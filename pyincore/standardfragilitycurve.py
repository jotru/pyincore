# Copyright (c) 2019 University of Illinois and others. All rights reserved.
#
# This program and the accompanying materials are made available under the
# terms of the Mozilla Public License v2.0 which accompanies this distribution,
# and is available at https://www.mozilla.org/en-US/MPL/2.0/

from pyincore.dfr3curve import DFR3Curve


class StandardFragilityCurve(DFR3Curve):

    def __init__(self, curve_parameters):
        self.alpha = curve_parameters['alpha']
        self.beta = curve_parameters['beta']
        self.alphaType = curve_parameters['alphaType']
        self.curveType = curve_parameters['curveType']

        super(StandardFragilityCurve, self).__init__(curve_parameters)

    def compute_limit_state(self):
        pass

    def plot(self):
        pass


