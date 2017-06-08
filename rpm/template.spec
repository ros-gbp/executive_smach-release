Name:           ros-jade-smach-ros
Version:        2.0.1
Release:        0%{?dist}
Summary:        ROS smach_ros package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib
Requires:       ros-jade-actionlib-msgs
Requires:       ros-jade-rospy
Requires:       ros-jade-rostopic
Requires:       ros-jade-smach
Requires:       ros-jade-smach-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-std-srvs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-rostest

%description
The smach_ros package contains extensions for the SMACH library to integrate it
tightly with ROS. For example, SMACH-ROS can call ROS services, listen to ROS
topics, and integrate with actionlib both as a client, and a provider of action
servers. SMACH is a new library that takes advantage of very old concepts in
order to quickly create robust robot behavior with maintainable and modular
code.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Jun 08 2017 Isaac I. Y. Saito <gm130s@gmail.com> - 2.0.1-0
- Autogenerated by Bloom

* Thu Apr 30 2015 Jonathan Bohren <jbo@jhu.edu> - 2.0.0-0
- Autogenerated by Bloom

