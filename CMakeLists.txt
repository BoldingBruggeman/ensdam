cmake_minimum_required( VERSION 3.15 )

#list( APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake )

set(CMAKE_POSITION_INDEPENDENT_CODE ON)

project( ensdam VERSION 1.0 LANGUAGES Fortran C )

add_subdirectory(src)
#add_subdirectory(python EXCLUDE_FROM_ALL)

add_custom_target(fortran DEPENDS ${PROJECT_NAME}_static ${PROJECT_NAME}_shared)
add_dependencies(fortran fortran)
#add_custom_target(python)
#add_dependencies(python fortran wheel)

add_subdirectory(examples EXCLUDE_FROM_ALL)
