// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from msg_interfaces:msg/GpsData.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "msg_interfaces/msg/detail/gps_data__rosidl_typesupport_introspection_c.h"
#include "msg_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "msg_interfaces/msg/detail/gps_data__functions.h"
#include "msg_interfaces/msg/detail/gps_data__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void msg_interfaces__msg__GpsData__rosidl_typesupport_introspection_c__GpsData_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  msg_interfaces__msg__GpsData__init(message_memory);
}

void msg_interfaces__msg__GpsData__rosidl_typesupport_introspection_c__GpsData_fini_function(void * message_memory)
{
  msg_interfaces__msg__GpsData__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember msg_interfaces__msg__GpsData__rosidl_typesupport_introspection_c__GpsData_message_member_array[5] = {
  {
    "latitude",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(msg_interfaces__msg__GpsData, latitude),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "longitude",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(msg_interfaces__msg__GpsData, longitude),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "velocity",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(msg_interfaces__msg__GpsData, velocity),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "satelites",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(msg_interfaces__msg__GpsData, satelites),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "hdop",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(msg_interfaces__msg__GpsData, hdop),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers msg_interfaces__msg__GpsData__rosidl_typesupport_introspection_c__GpsData_message_members = {
  "msg_interfaces__msg",  // message namespace
  "GpsData",  // message name
  5,  // number of fields
  sizeof(msg_interfaces__msg__GpsData),
  msg_interfaces__msg__GpsData__rosidl_typesupport_introspection_c__GpsData_message_member_array,  // message members
  msg_interfaces__msg__GpsData__rosidl_typesupport_introspection_c__GpsData_init_function,  // function to initialize message memory (memory has to be allocated)
  msg_interfaces__msg__GpsData__rosidl_typesupport_introspection_c__GpsData_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t msg_interfaces__msg__GpsData__rosidl_typesupport_introspection_c__GpsData_message_type_support_handle = {
  0,
  &msg_interfaces__msg__GpsData__rosidl_typesupport_introspection_c__GpsData_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_msg_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, msg_interfaces, msg, GpsData)() {
  if (!msg_interfaces__msg__GpsData__rosidl_typesupport_introspection_c__GpsData_message_type_support_handle.typesupport_identifier) {
    msg_interfaces__msg__GpsData__rosidl_typesupport_introspection_c__GpsData_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &msg_interfaces__msg__GpsData__rosidl_typesupport_introspection_c__GpsData_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
