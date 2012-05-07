"""
A single IF neuron with exponential, conductance-based synapses, fed by two
spike sources.

Run as:

$ python IF_cond_exp.py <simulator>

where <simulator> is 'neuron', 'nest', etc

Andrew Davison, UNIC, CNRS
May 2006

$Id: IF_cond_exp.py 917 2011-01-31 15:23:34Z apdavison $
"""

from pyNN.utility import get_script_args
from pyNN.errors import RecordingError

from pyNN.nest import *
import numpy as np

setup(timestep=0.1,min_delay=0.1,max_delay=4.0)

ifcell = create(IF_cond_exp, {  'i_offset' : 0.1,    'tau_refrac' : 3.0,
                                'v_thresh' : -51.0,  'tau_syn_E'  : 2.0,
                                'tau_syn_I': 5.0,    'v_reset'    : -70.0,
                                'e_rev_E'  : 0.,     'e_rev_I'    : -80.})

input_spikes = [float(i) for i in range(0,1000,10)]
spike_sourceE = create(SpikeSourceArray, {'spike_times': input_spikes})

connE = connect(spike_sourceE, ifcell, weight=0.06, synapse_type='excitatory',delay=2.0)
    
record_v(ifcell, "Results/IF_cond_exp.v")
record(ifcell, "Results/spikes.dat")
np.savetxt("Results/input_spikes.dat",input_spikes)

try:
    record_gsyn(ifcell, "Results/IF_cond_exp_nest=gsyn")
except (NotImplementedError, RecordingError):
    pass
run(1000.0)

end()