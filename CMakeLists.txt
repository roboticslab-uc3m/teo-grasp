cmake_minimum_required(VERSION 3.16)

project(TEO_GRASP LANGUAGES NONE)

# Hard dependencies.
find_package(YCM 0.11 REQUIRED)
find_package(YARP 3.7 REQUIRED)

# Configure installation paths for YARP resources.
yarp_configure_external_installation(teo-grasp)

# Define and enter subdirectories.
add_subdirectory(share)

# Configure and create uninstall target.
include(AddUninstallTarget)
