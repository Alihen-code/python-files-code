distance_mi = 1
is_raining = False
has_bike = False
has_car = False
has_ride_share_app = False
if not distance_mi:
    print(False)
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
elif 1 < distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
else:
    if has_ride_share_app or has_car:
        print(True)
    else:
        print(False)