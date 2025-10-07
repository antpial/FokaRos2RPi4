// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from msg_interfaces:msg/GpsData.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__MSG__DETAIL__GPS_DATA__STRUCT_HPP_
#define MSG_INTERFACES__MSG__DETAIL__GPS_DATA__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__msg_interfaces__msg__GpsData __attribute__((deprecated))
#else
# define DEPRECATED__msg_interfaces__msg__GpsData __declspec(deprecated)
#endif

namespace msg_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct GpsData_
{
  using Type = GpsData_<ContainerAllocator>;

  explicit GpsData_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->latitude = 0.0f;
      this->longitude = 0.0f;
      this->velocity = 0.0f;
      this->satelites = 0.0f;
      this->hdop = 0.0f;
    }
  }

  explicit GpsData_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->latitude = 0.0f;
      this->longitude = 0.0f;
      this->velocity = 0.0f;
      this->satelites = 0.0f;
      this->hdop = 0.0f;
    }
  }

  // field types and members
  using _latitude_type =
    float;
  _latitude_type latitude;
  using _longitude_type =
    float;
  _longitude_type longitude;
  using _velocity_type =
    float;
  _velocity_type velocity;
  using _satelites_type =
    float;
  _satelites_type satelites;
  using _hdop_type =
    float;
  _hdop_type hdop;

  // setters for named parameter idiom
  Type & set__latitude(
    const float & _arg)
  {
    this->latitude = _arg;
    return *this;
  }
  Type & set__longitude(
    const float & _arg)
  {
    this->longitude = _arg;
    return *this;
  }
  Type & set__velocity(
    const float & _arg)
  {
    this->velocity = _arg;
    return *this;
  }
  Type & set__satelites(
    const float & _arg)
  {
    this->satelites = _arg;
    return *this;
  }
  Type & set__hdop(
    const float & _arg)
  {
    this->hdop = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    msg_interfaces::msg::GpsData_<ContainerAllocator> *;
  using ConstRawPtr =
    const msg_interfaces::msg::GpsData_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<msg_interfaces::msg::GpsData_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<msg_interfaces::msg::GpsData_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::msg::GpsData_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::msg::GpsData_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      msg_interfaces::msg::GpsData_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<msg_interfaces::msg::GpsData_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<msg_interfaces::msg::GpsData_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<msg_interfaces::msg::GpsData_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__msg_interfaces__msg__GpsData
    std::shared_ptr<msg_interfaces::msg::GpsData_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__msg_interfaces__msg__GpsData
    std::shared_ptr<msg_interfaces::msg::GpsData_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GpsData_ & other) const
  {
    if (this->latitude != other.latitude) {
      return false;
    }
    if (this->longitude != other.longitude) {
      return false;
    }
    if (this->velocity != other.velocity) {
      return false;
    }
    if (this->satelites != other.satelites) {
      return false;
    }
    if (this->hdop != other.hdop) {
      return false;
    }
    return true;
  }
  bool operator!=(const GpsData_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GpsData_

// alias to use template instance with default allocator
using GpsData =
  msg_interfaces::msg::GpsData_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace msg_interfaces

#endif  // MSG_INTERFACES__MSG__DETAIL__GPS_DATA__STRUCT_HPP_
