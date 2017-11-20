# Copyright: Universidad Carlos III de Madrid (C) 2017
# Authors: Raúl de Santos Rico
# CopyPolicy: Released under the terms of the LGPLv2.1

set(KEYWORD "exampleProgram")

# Find YARP.
find_package(YARP REQUIRED)

# Retrieve global include paths and libraries.
get_property(teo-grasp_INCLUDE_DIRS GLOBAL PROPERTY teo-grasp_INCLUDE_DIRS)
get_property(teo-grasp_LIBRARIES GLOBAL PROPERTY teo-grasp_LIBRARIES)

# Define include paths.
include_directories(${YARP_INCLUDE_DIRS} ${teo-grasp_INCLUDE_DIRS})

# Configure executable build target.
add_executable(${KEYWORD} main.cpp ExampleProgram.cpp ExampleProgram.hpp)

# Link external libraries.
target_link_libraries(${KEYWORD} ${YARP_LIBRARIES} ${teo-grasp_LIBRARIES})

# Create installation rule.
install(TARGETS ${KEYWORD}
        DESTINATION ${CMAKE_INSTALL_BINDIR}
        COMPONENT example_program)

