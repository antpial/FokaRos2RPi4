// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from msg_interfaces:msg/GpsData.idl
// generated code does not contain a copyright notice

#ifndef MSG_INTERFACES__MSG__DETAIL__GPS_DATA__STRUCT_H_
#define MSG_INTERFACES__MSG__DETAIL__GPS_DATA__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/GpsData in the package msg_interfaces.
typedef struct msg_interfaces__msg__GpsData
{
  float latitude;
  float longitude;
  float velocity;
  float satelites;
  float hdop;
} msg_interfaces__msg__GpsData;

// Struct for a sequence of msg_interfaces__msg__GpsData.
typedef struct msg_interfaces__msg__GpsData__Sequence
{
  msg_interfaces__msg__GpsData * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} msg_interfaces__msg__GpsData__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MSG_INTERFACES__MSG__DETAIL__GPS_DATA__STRUCT_H_
