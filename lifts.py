chinups_start = 0.0
press_start = 60.0
bench_start = 115.0
squat_start = 125.0
deadlift_start = 150.0
rows_start = 105.0

chinups = chinups_start
press = press_start
bench = bench_start
squat = squat_start
deadlift =  deadlift_start
rows = rows_start

weight1 = [press, bench]
weight2 = [chinups, rows]
weight3 = [squat, deadlift]

lift1 = ["Overhead Press", "Bench Press"]
lift2 = ["Chinups", "Bent-over Row"]
lift3 = ["Squat", "Deadlift"]

week_num = 1
day_num = 1

small_inc = 2.5
big_inc = 5.0

l1_var = 0
l2_var = 0
l3_var = 0

def print_lifts():
  print "Week", week_num, ", Day", day_num
  print "Lift #1:", lift1[l1_var], "@", myround(weight1[l1_var]), "lbs"
  print "Lift #2:", lift2[l2_var], "@", myround(weight2[l2_var]), "lbs"
  print "Lift #3:", lift3[l3_var], "@", myround(weight3[l3_var]), "lbs"
  print "\n"

def finish_workout():
  global l1_var, l2_var, l3_var, day_num, week_num, weight1, weight2, weight3

  lift1_reps = int(raw_input('How many AMRAP reps of ' + lift1[l1_var] + ' did you do? '))
  lift2_reps = int(raw_input('How many AMRAP reps of ' + lift2[l2_var] + ' did you do? '))
  lift3_reps = int(raw_input('How many AMRAP reps of ' + lift3[l3_var] + ' did you do? '))
  print "\n"

  # Checks for increase/decrease of weight for next workout
  if lift1_reps < 5:
    weight1[l1_var] *= 0.9
  elif lift1_reps >= 10:
    weight1[l1_var] += (2.0 * small_inc)
  else:
    weight1[l1_var] += small_inc

  if lift2_reps < 5:
    weight2[l2_var] *= 0.9
  elif lift2_reps >= 10:
    weight2[l2_var] += (2.0 * small_inc)
  else:
    weight2[l2_var] += small_inc

  if lift3_reps < 5:
    weight3[l3_var] *= 0.9
  elif lift3_reps >= 10:
    weight3[l3_var] += (2.0 * big_inc)
  else:
    weight3[l3_var] += big_inc

  # Switches between A/B exercises each workout
  if l1_var == 0:
    l1_var = 1
  else:
    l1_var = 0

  if l2_var == 0:
    l2_var = 1
  else:
    l2_var = 0

  # Switches between deadlift and squat
  if day_num == 1:
    l3_var = 0
  if day_num == 2:
    l3_var = 1
  if day_num == 3:
    l3_var = 0

  # Sets the day_num between 1 and 3 and increase the week
  if day_num < 3:
    day_num += 1
  else:
    day_num = 1
    week_num += 1

  print "\n"

# Rounds to nearest 2.5
def myround(x, base=2.5):
  return float(base*round(float(x)/base))
