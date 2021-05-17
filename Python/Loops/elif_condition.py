 # elif is used to check more than just one condition, and to stop when the first statement which is true is found.

 if the_weather_is_good
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()

# you mustn't use else without a preceding if;
# else is always the last branch of the cascade, regardless of whether you've used elif or not;
# else is an optional part of the cascade, and may be omitted;
# if there is an else branch in the cascade, only one of all the branches is executed;
# if there is no else branch, it's possible that none of the available branches is executed.