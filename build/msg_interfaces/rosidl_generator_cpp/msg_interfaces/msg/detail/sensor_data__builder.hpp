// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from msg_interfaces:msg/SensorData.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__MSG__DETAIL__SENSOR_DATA__BUILDER_HPP_
#define MSG_INTERFACES__MSG__DETAIL__SENSOR_DATA__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "msg_interfaces/msg/detail/sensor_data__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace msg_interfaces
{

namespace msg
{

namespace builder
{

class Init_SensorData_stamp
{
public:
  explicit Init_SensorData_stamp(::msg_interfaces::msg::SensorData & msg)
  : msg_(msg)
  {}
  ::msg_interfaces::msg::SensorData stamp(::msg_interfaces::msg::SensorData::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::msg_interfaces::msg::SensorData msg_;
};

class Init_SensorData_longitude
{
public:
  explicit Init_SensorData_longitude(::msg_interfaces::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_stamp longitude(::msg_interfaces::msg::SensorData::_longitude_type arg)
  {
    msg_.longitude = std::move(arg);
    return Init_SensorData_stamp(msg_);
  }

private:
  ::msg_interfaces::msg::SensorData msg_;
};

class Init_SensorData_latitude
{
public:
  explicit Init_SensorData_latitude(::msg_interfaces::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_longitude latitude(::msg_interfaces::msg::SensorData::_latitude_type arg)
  {
    msg_.latitude = std::move(arg);
    return Init_SensorData_longitude(msg_);
  }

private:
  ::msg_interfaces::msg::SensorData msg_;
};

class Init_SensorData_conductivity
{
public:
  explicit Init_SensorData_conductivity(::msg_interfaces::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_latitude conductivity(::msg_interfaces::msg::SensorData::_conductivity_type arg)
  {
    msg_.conductivity = std::move(arg);
    return Init_SensorData_latitude(msg_);
  }

private:
  ::msg_interfaces::msg::SensorData msg_;
};

class Init_SensorData_ph
{
public:
  explicit Init_SensorData_ph(::msg_interfaces::msg::SensorData & msg)
  : msg_(msg)
  {}
  Init_SensorData_conductivity ph(::msg_interfaces::msg::SensorData::_ph_type arg)
  {
    msg_.ph = std::move(arg);
    return Init_SensorData_conductivity(msg_);
  }

private:
  ::msg_interfaces::msg::SensorData msg_;
};

class Init_SensorData_temperature
{
public:
  Init_SensorData_temperature()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SensorData_ph temperature(::msg_interfaces::msg::SensorData::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return Init_SensorData_ph(msg_);
  }

private:
  ::msg_interfaces::msg::SensorData msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::msg_interfaces::msg::SensorData>()
{
  return msg_interfaces::msg::builder::Init_SensorData_temperature();
}

}  // namespace msg_interfaces

#endif  // MSG_INTERFACES__MSG__DETAIL__SENSOR_DATA__BUILDER_HPP_
