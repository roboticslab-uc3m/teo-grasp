# Store the package in the user registry.
export(PACKAGE teo-grasp)

# Retrieve global properties.
get_property(teo-grasp_INCLUDE_DIRS GLOBAL PROPERTY teo-grasp_INCLUDE_DIRS)
get_property(teo-grasp_TARGETS GLOBAL PROPERTY teo-grasp_TARGETS)
get_property(_teo-grasp_LIBRARIES GLOBAL PROPERTY teo-grasp_LIBRARIES)

# Append namespace prefix to exported libraries.
set(teo-grasp_LIBRARIES)
foreach(lib ${_teo-grasp_LIBRARIES})
  list(APPEND teo-grasp_LIBRARIES teo-grasp::${lib})
endforeach()
unset(_teo-grasp_LIBRARIES) # just in case

# Set build/install pairs of paths for each exported property.
set(teo-grasp_BUILD_INCLUDE_DIRS ${teo-grasp_INCLUDE_DIRS})
set(teo-grasp_INSTALL_INCLUDE_DIRS ${CMAKE_INSTALL_FULL_INCLUDEDIR})

# Create and install config and version files (YCM).
include(InstallBasicPackageFiles)

install_basic_package_files(teo-grasp
                            VERSION ${teo-grasp_VERSION_SHORT}
                            COMPATIBILITY AnyNewerVersion
                            TARGETS_PROPERTY teo-grasp_TARGETS
                            NO_CHECK_REQUIRED_COMPONENTS_MACRO
                            EXTRA_PATH_VARS_SUFFIX INCLUDE_DIRS)

# Configure and create uninstall target (YCM).
include(AddUninstallTarget)

