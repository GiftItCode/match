create table if not exists Mentor (
id integer primary key,
email text not null,
full_name text not null,
preferred_name text,
join_date text not null
);

create table if not exists SkillType (
id integer primary key,
code text not null,
description text not null
);

create table if not exists Skill (
id integer primary key,
code text not null,
skill_type integer not null,
description text not null
);

create table if not exists DayOfWeek (
id integer primary key,
name text not null
);

create table if not exists Timeslot (
id integer primary key,
begin_time text not null,
end_time text not null,
day_of_week integer not null,
foreign key (day_of_week) references dayofweek (id)
);

create table if not exists MentorAvailabilitySlots (
id integer primary key,
skill_id integer not null,
mentor_id integer not null,
slot_begin_id integer not null,
slot_end_id integer not null,
date_begin text not null,
date_end text not null,
active integer not null,
foreign key (skill_id) references Skill (id),
foreign key (mentor_id) references Mentor (id),
foreign key (slot_begin_id) references Timeslot (id),
foreign key (slot_end_id) references Timeslot (id)
);
