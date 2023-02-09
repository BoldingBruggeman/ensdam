set(CMAKE_POSITION_INDEPENDENT_CODE ON)

add_library(censdam pyensdam_wrapper.F90)
target_link_libraries(censdam ensdam_static)

add_custom_command(OUTPUT ${CMAKE_CURRENT_SOURCE_DIR}/_pyensdam.c
  COMMAND cython _pyensdam.pyx
  MAIN_DEPENDENCY _pyensdam.pyx
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
)

Python3_add_library(_pyensdam MODULE _pyensdam.c)
target_link_libraries(_pyensdam PRIVATE censdam Python3::NumPy)
