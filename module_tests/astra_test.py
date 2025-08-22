# This script is for testing if ASTRA Toolbox can make use of a local GPU, which is necessary to run GPU-accelerated ODL code. 
# For labs 1 and 2, GPU acceleration is not necessary. For labs 3 and 4, the plan is to provide access to a server with an appropriate GPU.

import astra

astra.test()
