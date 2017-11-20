# Copyright: Universidad Carlos III de Madrid (C) 2017
# Authors: Raúl de Santos Rico
# CopyPolicy: Released under the terms of the LGPLv2.1

cmake_minimum_required(VERSION 2.8.9 FATAL_ERROR)

# Start a project.
project(teo-grasp)

# Set module path.
set(teo-grasp_MODULE_PATH ${CMAKE_SOURCE_DIR}/cmake)
list(APPEND CMAKE_MODULE_PATH ${teo-grasp_MODULE_PATH})

# Bootstrap YCM.
# https://github.com/robotology/ycm/issues/118
set(YCM_TAG v0.2.2)
include(YCMBootstrap)

# Retrieve current teo-grasp version.
include(teo-graspVersion)

# Define standard paths, check system configuration.
include(teo-graspSystem)

# Setup build options.
include(teo-graspOptions)

# Define global properties to store relevant configuration.
set_property(GLOBAL PROPERTY teo-grasp_INCLUDE_DIRS)
set_property(GLOBAL PROPERTY teo-grasp_LIBRARIES)
set_property(GLOBAL PROPERTY teo-grasp_TARGETS)

# Define and enter subdirectories.
add_subdirectory(share)
add_subdirectory(libraries)
add_subdirectory(programs)

# Output configuration files.
include(teo-graspDescribe)

# Create target for documentation generation.
include(teo-graspDoc)

# Invoke CPack from here.
include(teo-graspPackage)

# Generate a report of enabled/disabled features.
feature_summary(FATAL_ON_MISSING_REQUIRED_PACKAGES WHAT ALL)

