#
# Model class
#

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, V_c, V_p1, q_c, q_p1, CL, Q_p1): # need to make suitable for more than one compartment maybe
        self.V_c = V_c
	self.V_p1 = V_p1
	self.q_c = q_c
	self.q_p1 = q_p1
	self.CL = CL
	self.Q_p1 = Q_p1


