"""
test_invoice_engine.py - Automated Unit Tests for Ledgerly Invoice Generator
Covers Experiment 10 requirements: Automated unit tests for core application logic.
"""

import unittest

def calculate_subtotal(items):
    """Calculate subtotal from a list of items: each item has 'qty' and 'price'."""
    return sum(item.get('qty', 0) * item.get('price', 0.0) for item in items)

def calculate_discount(subtotal, discount_type, discount_val):
    """Calculate discount amount based on percentage or flat value."""
    if discount_val < 0:
        raise ValueError("Discount value cannot be negative")
    if discount_type == 'percent':
        if discount_val > 100:
            raise ValueError("Discount percentage cannot exceed 100%")
        return (subtotal * discount_val) / 100.0
    return min(subtotal, float(discount_val))

def calculate_tax(taxable_amount, tax_rate, is_interstate=False):
    """
    Calculate GST breakdown.
    If is_interstate is True: returns {'igst': tax_amt, 'cgst': 0, 'sgst': 0}
    If is_interstate is False: returns {'igst': 0, 'cgst': tax_amt/2, 'sgst': tax_amt/2}
    """
    if tax_rate < 0 or tax_rate > 100:
        raise ValueError("Tax rate must be between 0 and 100")
    total_tax = (taxable_amount * tax_rate) / 100.0
    if is_interstate:
        return {'igst': round(total_tax, 2), 'cgst': 0.0, 'sgst': 0.0, 'total_tax': round(total_tax, 2)}
    half_tax = round(total_tax / 2.0, 2)
    return {'igst': 0.0, 'cgst': half_tax, 'sgst': half_tax, 'total_tax': round(half_tax * 2, 2)}

def calculate_grand_total(subtotal, discount_amt, tax_amt, extra_charges=0.0, auto_round=False):
    """Calculate final grand total with optional rounding."""
    pre_round = (subtotal - discount_amt) + tax_amt + extra_charges
    if auto_round:
        rounded_total = round(pre_round)
        round_off = round(rounded_total - pre_round, 2)
        return rounded_total, round_off
    return round(pre_round, 2), 0.0

def determine_payment_status(grand_total, total_paid):
    """Determine payment status based on amount settled."""
    if total_paid <= 0:
        return "Unpaid"
    elif total_paid < grand_total:
        return "Partially Paid"
    return "Paid"

def validate_user_registration(name, email, password, phone):
    """Validate registration fields."""
    if not name or len(name.strip()) < 3:
        return False, "Name must be at least 3 characters"
    if "@" not in email or "." not in email:
        return False, "Invalid email address format"
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    if len(phone) != 10 or not phone.isdigit():
        return False, "Phone number must be exactly 10 digits"
    return True, "Registration Valid"


class TestInvoiceEngine(unittest.TestCase):

    def test_tc_calc_01_subtotal(self):
        """TC_CALC_01: Verify multi-item subtotal calculation."""
        items = [
            {'name': 'Web Design', 'qty': 2, 'price': 1500.0},
            {'name': 'Hosting Setup', 'qty': 1, 'price': 800.0}
        ]
        self.assertEqual(calculate_subtotal(items), 3800.0)

    def test_tc_calc_02_percentage_discount(self):
        """TC_CALC_02: Verify percentage discount calculation."""
        subtotal = 5000.0
        discount = calculate_discount(subtotal, 'percent', 10)
        self.assertEqual(discount, 500.0)

    def test_tc_calc_03_flat_discount(self):
        """TC_CALC_03: Verify flat cash discount calculation."""
        subtotal = 5000.0
        discount = calculate_discount(subtotal, 'flat', 750)
        self.assertEqual(discount, 750.0)

    def test_tc_calc_04_discount_boundary_error(self):
        """TC_CALC_04: Negative discount or >100% must raise ValueError."""
        with self.assertRaises(ValueError):
            calculate_discount(1000, 'percent', 105)
        with self.assertRaises(ValueError):
            calculate_discount(1000, 'flat', -50)

    def test_tc_tax_01_intrastate_gst(self):
        """TC_TAX_01: Intra-state supply splits evenly into CGST and SGST (9% + 9%)."""
        taxable = 1000.0
        breakdown = calculate_tax(taxable, 18.0, is_interstate=False)
        self.assertEqual(breakdown['cgst'], 90.0)
        self.assertEqual(breakdown['sgst'], 90.0)
        self.assertEqual(breakdown['igst'], 0.0)
        self.assertEqual(breakdown['total_tax'], 180.0)

    def test_tc_tax_02_interstate_gst(self):
        """TC_TAX_02: Inter-state supply routes 100% to IGST."""
        taxable = 1000.0
        breakdown = calculate_tax(taxable, 18.0, is_interstate=True)
        self.assertEqual(breakdown['igst'], 180.0)
        self.assertEqual(breakdown['cgst'], 0.0)
        self.assertEqual(breakdown['sgst'], 0.0)

    def test_tc_total_01_auto_round_off(self):
        """TC_TOT_01: Verify automatic integer rounding and round-off delta."""
        # 1000 subtotal - 0 disc + 45.35 tax = 1045.35 -> 1045.0, delta -0.35
        grand_total, delta = calculate_grand_total(1000.0, 0.0, 45.35, 0.0, auto_round=True)
        self.assertEqual(grand_total, 1045.0)
        self.assertEqual(delta, -0.35)

    def test_tc_pay_01_unpaid_status(self):
        """TC_PAY_01: 0 payments settled results in Unpaid status."""
        self.assertEqual(determine_payment_status(5000.0, 0.0), "Unpaid")

    def test_tc_pay_02_partial_payment(self):
        """TC_PAY_02: Payment less than grand total results in Partially Paid."""
        self.assertEqual(determine_payment_status(5000.0, 2000.0), "Partially Paid")

    def test_tc_pay_03_full_settlement(self):
        """TC_PAY_03: Payment equal to or exceeding grand total results in Paid."""
        self.assertEqual(determine_payment_status(5000.0, 5000.0), "Paid")
        self.assertEqual(determine_payment_status(5000.0, 5500.0), "Paid")

    def test_tc_val_01_valid_registration(self):
        """TC_VAL_01: Valid user inputs pass verification."""
        valid, msg = validate_user_registration("Krushna Patil", "krushna@example.com", "pass1234", "9876543210")
        self.assertTrue(valid)

    def test_tc_val_02_invalid_phone(self):
        """TC_VAL_02: Non-10 digit phone fails validation."""
        valid, msg = validate_user_registration("Krushna Patil", "krushna@example.com", "pass1234", "98765")
        self.assertFalse(valid)
        self.assertIn("10 digits", msg)


if __name__ == '__main__':
    unittest.main()
