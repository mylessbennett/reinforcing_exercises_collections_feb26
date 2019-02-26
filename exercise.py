dict = { 'data': { 'rooms':
    [ { 'id': 1, 'room_number': "201", 'capacity': 50}, { 'id': 2, 'room_number': "301", 'capacity': 200 },
    { 'id': 3, 'room_number': "1B", 'capacity': 100}
    ],
    'events': [
      { 'id': 1, 'room_id': 2, 'start_time': 18, 'end_time': 20, 'attendees': 75 },
      { 'id': 2, 'room_id': 1, 'start_time': 10, 'end_time': 18, 'attendees': 25 },
      { 'id': 3, 'room_id': 2, 'start_time': 10, 'end_time': 18, 'attendees': 20 },
      { 'id': 4, 'room_id': 3, 'start_time': 18, 'end_time': 21, 'attendees': 56 },
    ]
  }
}


# Exercise 1
# -----------------------------------------------------------------------
room201_capacity = dict['data']['rooms'][0]['capacity']
print(room201_capacity)

# Exercise 2
# -----------------------------------------------------------------------
for key in dict['data']['events']:
    if key['room_id'] == 1 and key['attendees'] <= 50:
        print("Event {} will fit".format(key['id']))
    else:
        print("Event {} will not fit".format(key['id']))
