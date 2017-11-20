# Copyright: Universidad Carlos III de Madrid (C) 2017
# Authors: Raúl de Santos Rico
# CopyPolicy: Released under the terms of the LGPLv2.1

set(KEYWORD "ExampleLibrary")

# Find YARP.
find_package(YARP REQUIRED)

# Add current directory to global include paths, retrieve current values.
set_property(GLOBAL APPEND PROPERTY teo-grasp_INCLUDE_DIRS "${CMAKE_CURRENT_SOURCE_DIR}")
get_property(teo-grasp_INCLUDE_DIRS GLOBAL PROPERTY teo-grasp_INCLUDE_DIRS)

# Define include paths.
include_directories(${YARP_INCLUDE_DIRS} ${teo-grasp_INCLUDE_DIRS})

# Configure library build target.
add_library(${KEYWORD} ExampleLibrary.cpp ExampleLibrary.hpp)

# Link external libraries.
target_link_libraries(${KEYWORD} LINK_PRIVATE ${YARP_LIBRARIES})

# Create installation rule.
install(TARGETS ${KEYWORD}
        EXPORT teo-grasp
        LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR} COMPONENT example_library
        ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR} COMPONENT example_library
        RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR} COMPONENT example_library)

# Export library name and current target.
set_property(GLOBAL APPEND PROPERTY teo-grasp_LIBRARIES ${KEYWORD})
set_property(GLOBAL APPEND PROPERTY teo-grasp_TARGETS ${KEYWORD})
