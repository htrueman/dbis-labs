CREATE KEYSPACE IF NOT EXISTS lecture_vcs WITH replication = {
	'class': 'SimpleStrategy',
	'replication_factor': '1'
};

CREATE TYPE IF NOT EXISTS lecture_vcs.user_data (
   role varchar,
   date_registered date,
);

CREATE TABLE IF NOT EXISTS lecture_vcs.users (
 user_id int,
 email varchar,
 data frozen<user_data>,

 subjects set<int>,
 PRIMARY KEY (user_id),
);

CREATE TABLE IF NOT EXISTS lecture_vcs.groups (
 group_id int,
 user_id int,

 group_name varchar,
 user_email varchar,
 PRIMARY KEY ((group_id, user_id), group_name)
);

CREATE TABLE IF NOT EXISTS lecture_vcs.subjects (
 subject_id int,
 name text,
 users set<int>,
 lecturer_id int,
 group_id int,
 lecture_id int,

 PRIMARY KEY (lecture_id, subject_id, group_id)
);

CREATE TABLE IF NOT EXISTS lecture_vcs.lectures (
    lecture_id int,
    prev_version_lecture_id int,
    version text,
    created timestamp,
    modified timestamp,
    meta map<text, frozen <list<text>>>,

    PRIMARY KEY (lecture_id, version)
);

CREATE TABLE IF NOT EXISTS lecture_vcs.lecture_pack (
    pack_id int,
    lecture_id int,

    pack_name text,
    description text,

    PRIMARY KEY (lecture_id, pack_id)
);


CREATE TABLE IF NOT EXISTS lecture_vcs.lecture_comment (
    text text,
    datetime timestamp static,
    likes int,
    comment_id int,
    lecture_id int,

    PRIMARY KEY (lecture_id, comment_id)
);

CREATE TABLE IF NOT EXISTS lecture_vcs.lecture_activity (
    view_count int,
    like_count int,
    comment_count int,
    lecture_activity_id int,
    user_id int,
    lecture_id int,

    PRIMARY KEY (lecture_id, lecture_activity_id, user_id)
);