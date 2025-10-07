// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from msg_interfaces:msg/SensorData.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__MSG__DETAIL__SENSOR_DATA__STRUCT_H_
#define MSG_INTERFACES__MSG__DETAIL__SENSOR_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in msg/SensorData in the package msg_interfaces.
typedef struct msg_interfaces__msg__SensorData
{
  float temperature;
  float ph;
  float conductivity;
  double latitude;
  double longitude;
  builtin_interfaces__msg__Time stamp;
} msg_interfaces__msg__SensorData;

// Struct for a sequence of msg_interfaces__msg__SensorData.
typedef struct msg_interfaces__msg__SensorData__Sequence
{
  msg_interfaces__msg__SensorData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_interfaces__msg__SensorData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MSG_INTERFACES__MSG__DETAIL__SENSOR_DATA__STRUCT_H_
