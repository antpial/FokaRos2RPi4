// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from msg_interfaces:msg/GpsData.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__MSG__DETAIL__GPS_DATA__BUILDER_HPP_
#define MSG_INTERFACES__MSG__DETAIL__GPS_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "msg_interfaces/msg/detail/gps_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace msg_interfaces
{

namespace msg
{

namespace builder
{

class Init_GpsData_hdop
{
public:
  explicit Init_GpsData_hdop(::msg_interfaces::msg::GpsData & msg)
  : msg_(msg)
  {}
  ::msg_interfaces::msg::GpsData hdop(::msg_interfaces::msg::GpsData::_hdop_type arg)
  {
    msg_.hdop = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_interfaces::msg::GpsData msg_;
};

class Init_GpsData_satelites
{
public:
  explicit Init_GpsData_satelites(::msg_interfaces::msg::GpsData & msg)
  : msg_(msg)
  {}
  Init_GpsData_hdop satelites(::msg_interfaces::msg::GpsData::_satelites_type arg)
  {
    msg_.satelites = std::move(arg);
    return Init_GpsData_hdop(msg_);
  }

private:
  ::msg_interfaces::msg::GpsData msg_;
};

class Init_GpsData_velocity
{
public:
  explicit Init_GpsData_velocity(::msg_interfaces::msg::GpsData & msg)
  : msg_(msg)
  {}
  Init_GpsData_satelites velocity(::msg_interfaces::msg::GpsData::_velocity_type arg)
  {
    msg_.velocity = std::move(arg);
    return Init_GpsData_satelites(msg_);
  }

private:
  ::msg_interfaces::msg::GpsData msg_;
};

class Init_GpsData_longitude
{
public:
  explicit Init_GpsData_longitude(::msg_interfaces::msg::GpsData & msg)
  : msg_(msg)
  {}
  Init_GpsData_velocity longitude(::msg_interfaces::msg::GpsData::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return Init_GpsData_velocity(msg_);
  }

private:
  ::msg_interfaces::msg::GpsData msg_;
};

class Init_GpsData_latitude
{
public:
  Init_GpsData_latitude()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GpsData_longitude latitude(::msg_interfaces::msg::GpsData::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_GpsData_longitude(msg_);
  }

private:
  ::msg_interfaces::msg::GpsData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_interfaces::msg::GpsData>()
{
  return msg_interfaces::msg::builder::Init_GpsData_latitude();
}

}  // namespace msg_interfaces

#endif  // MSG_INTERFACES__MSG__DETAIL__GPS_DATA__BUILDER_HPP_
