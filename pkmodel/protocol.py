#
# Protocol class
#

class Protocol:
    """A Pharmokinetic (PK) protocol

    Parameters
    ----------

    dose_type: str
	Type of dosing being used (e.g. "IV" for IV bolus or "SC" for subcutaneous)
    k_a: float
	Absorption rate for s.c. dosing. 

    """
    def __init__(self, dose_type = "IV", k_a = None, dose_amount):
        self.dose_type = dose_type
        self.k_a = k_a
        self.doses = []
        self.dose_amount = dose_amount

    def add_dose(self, time: float, amount: float):
        self.doses.append = (time, amount)
    def dose_at_time(self, time: float):
        t = time
	return self.dose_amount
