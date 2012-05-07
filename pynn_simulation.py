### Simulation of two neurons with PyNN and NEST ###

# Imports
from pyNN.utility import get_script_args
from pyNN.errors import RecordingError
from pyNN.nest import *
import numpy as np

# Setup
setup(timestep=0.1,min_delay=0.1,max_delay=4.0)

# Neuron creation
ifcell = create(IF_cond_exp, {  'i_offset' : 0.1,    'tau_refrac' : 3.0,
                                'v_thresh' : -51.0,  'tau_syn_E'  : 2.0,
                                'tau_syn_I': 5.0,    'v_reset'    : -70.0,
                                'e_rev_E'  : 0.,     'e_rev_I'    : -80.})

# Input neuron
input_spikes = [float(i) for i in range(0,1000,10)]
spike_sourceE = create(SpikeSourceArray, {'spike_times': input_spikes})

# Connection between neurons
connE = connect(spike_sourceE, ifcell, weight=0.06, synapse_type='excitatory',delay=2.0)

# Save results    
record_v(ifcell, "Results/IF_cond_exp.v")
record(ifcell, "Results/spikes.dat")
np.savetxt("Results/input_spikes.dat",input_spikes)

# Start simulation for 1000 ms
run(1000.0)
end()