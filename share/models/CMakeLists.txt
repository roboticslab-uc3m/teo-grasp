# Copyright: 2017 UC3M
# Author: Raúl de Santos Rico
# CopyPolicy: Released under the terms of the GNU GPL v2.0.

set(appname models)

file(GLOB xml ${CMAKE_CURRENT_SOURCE_DIR}/*.xml)

yarp_install(FILES ${xml} DESTINATION ${TEO-GRASP_CONTEXTS_INSTALL_DIR}/${appname})
