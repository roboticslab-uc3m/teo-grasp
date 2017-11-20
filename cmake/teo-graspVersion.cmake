include(GitInfo) # YCM

# Define current version.
set(teo-grasp_VERSION_MAJOR 0)
set(teo-grasp_VERSION_MINOR 1)
set(teo-grasp_VERSION_PATCH 0)

set(teo-grasp_VERSION
    ${teo-grasp_VERSION_MAJOR}.${teo-grasp_VERSION_MINOR}.${teo-grasp_VERSION_PATCH})

set(teo-grasp_VERSION_SHORT ${teo-grasp_VERSION})

# Retrieve current revision from Git working tree.
git_wt_info(SOURCE_DIR "${CMAKE_SOURCE_DIR}"
            PREFIX teo-grasp)

if(DEFINED teo-grasp_GIT_WT_HASH)
    if(teo-grasp_GIT_WT_TAG_REVISION GREATER 0)
        set(teo-grasp_VERSION_REVISION ${teo-grasp_GIT_WT_TAG_REVISION})
        string(REPLACE "-" "" _date ${teo-grasp_GIT_WT_AUTHOR_DATE})
        set(teo-grasp_VERSION_SOURCE
            "${_date}.${teo-grasp_GIT_WT_DATE_REVISION}+git${teo-grasp_GIT_WT_HASH_SHORT}")
    endif()

    if(teo-grasp_GIT_WT_DIRTY)
        set(teo-grasp_VERSION_DIRTY "dirty")
    endif()
endif()

if(DEFINED teo-grasp_VERSION_SOURCE)
    if(NOT "${teo-grasp_GIT_WT_TAG}" STREQUAL "v${teo-grasp_VERSION_SHORT}")
        set(teo-grasp_VERSION
            "${teo-grasp_VERSION_SHORT}+${teo-grasp_VERSION_SOURCE}")
    else()
        set(teo-grasp_VERSION
           "${teo-grasp_VERSION_SHORT}+${teo-grasp_VERSION_REVISION}-${teo-grasp_VERSION_SOURCE}")
    endif()
elseif(NOT "${teo-grasp_GIT_WT_TAG}" STREQUAL "v${teo-grasp_VERSION_SHORT}")
    set(teo-grasp_VERSION "${teo-grasp_VERSION_SHORT}~dev")
else()
    set(teo-grasp_VERSION "${teo-grasp_VERSION_SHORT}")
endif()

if(DEFINED teo-grasp_VERSION_DIRTY)
    set(teo-grasp_VERSION "${teo-grasp_VERSION}+${teo-grasp_VERSION_DIRTY}")
endif()

# Print version.
message(STATUS "teo-grasp version: ${teo-grasp_VERSION_SHORT} (${teo-grasp_VERSION})")

