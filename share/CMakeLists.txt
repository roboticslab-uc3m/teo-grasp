# Copyright: Universidad Carlos III de Madrid (C) 2017
# Authors: Raúl de Santos Rico
# CopyPolicy: Released under the terms of the LGPLv2.1

find_package(YARP REQUIRED)
list(APPEND CMAKE_MODULE_PATH ${YARP_MODULE_PATH})
include(YarpInstallationHelpers)
yarp_configure_external_installation(teo-grasp)

### Go through single applications

add_subdirectory(models)

