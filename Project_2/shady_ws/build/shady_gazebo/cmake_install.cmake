# Install script for directory: /home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM690_Robot_Learning/Github/enpm690/Project_2/shady_ws/src/shady_gazebo

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM690_Robot_Learning/Github/enpm690/Project_2/shady_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM690_Robot_Learning/Github/enpm690/Project_2/shady_ws/build/shady_gazebo/catkin_generated/installspace/shady_gazebo.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/shady_gazebo/cmake" TYPE FILE FILES
    "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM690_Robot_Learning/Github/enpm690/Project_2/shady_ws/build/shady_gazebo/catkin_generated/installspace/shady_gazeboConfig.cmake"
    "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM690_Robot_Learning/Github/enpm690/Project_2/shady_ws/build/shady_gazebo/catkin_generated/installspace/shady_gazeboConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/shady_gazebo" TYPE FILE FILES "/home/nalindas9/Documents/Courses/Spring_2020_Semester_2/ENPM690_Robot_Learning/Github/enpm690/Project_2/shady_ws/src/shady_gazebo/package.xml")
endif()

