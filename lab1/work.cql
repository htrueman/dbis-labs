use lecture_vcs;

INSERT INTO users (user_id, email, data, subjects) VALUES (1, 'test1@mail.com', {"role": 'student', "date_registered": '2019-10-10'}, {1, 2, 3});
INSERT INTO users (user_id, email, data, subjects) VALUES (2, 'test2@mail.com', {"role": 'student', "date_registered": '2019-11-11'}, {2, 3, 4});
INSERT INTO users (user_id, email, data, subjects) VALUES (3, 'test3@mail.com', {"role": 'lecturer', "date_registered": '2019-11-12'}, {5, 6, 7});

SELECT * FROM users;


INSERT INTO groups (group_id, user_id, group_name, user_email) VALUES (1, 1, 'km-61', 'test1@mail.com');
INSERT INTO groups (group_id, user_id, group_name, user_email) VALUES (2, 2, 'km-62', 'test2@mail.com');
INSERT INTO groups (group_id, user_id, group_name, user_email) VALUES (3, 3, 'km-63', 'test3@mail.com');

SELECT * FROM groups;


INSERT INTO subjects (subject_id, name, users, lecturer_id, group_id, lecture_id) VALUES (1, 'calculus', {1, 2}, 3, 1, 1);
INSERT INTO subjects (subject_id, name, users, lecturer_id, group_id, lecture_id) VALUES (2, 'diff equations', {1, 2}, 3, 2, 2);
INSERT INTO subjects (subject_id, name, users, lecturer_id, group_id, lecture_id) VALUES (3, 'dbis', {1, 2}, 3, 3, 3);

SELECT * FROM subjects;


INSERT INTO lectures (lecture_id, version, created, modified, meta) VALUES (1, 'v1', '2019-10-10', '2019-10-11', {'tags': ['tag1', 'tag2']});
INSERT INTO lectures (lecture_id, version, created, modified, meta) VALUES (2, 'v2', '2019-10-11', '2019-10-12', {'tags': ['tag2', 'tag3']});
INSERT INTO lectures (lecture_id, version, created, modified, meta) VALUES (3, 'v3', '2019-10-12', '2019-10-13', {'tags': ['tag3', 'tag4']});

SELECT * FROM lectures;


INSERT INTO lecture_pack (pack_id, lecture_id, pack_name, description) VALUES (1, 1, 'pack1', 'desc1');
INSERT INTO lecture_pack (pack_id, lecture_id, pack_name, description) VALUES (2, 2, 'pack2', 'desc2');
INSERT INTO lecture_pack (pack_id, lecture_id, pack_name, description) VALUES (3, 3, 'pack3', 'desc3');
SELECT * FROM lecture_pack;


INSERT INTO lecture_comment (text, datetime, likes, comment_id, lecture_id) VALUES ('text1', '2019-11-10', 1, 1, 1);
INSERT INTO lecture_comment (text, datetime, likes, comment_id, lecture_id) VALUES ('text2', '2019-11-11', 2, 2, 2);
INSERT INTO lecture_comment (text, datetime, likes, comment_id, lecture_id) VALUES ('text3', '2019-11-12', 3, 3, 3);

SELECT * FROM lecture_comment;


INSERT INTO lecture_activity (view_count, like_count, comment_count, lecture_activity_id, user_id, lecture_id) VALUES (1, 1, 1, 1, 1, 1);
INSERT INTO lecture_activity (view_count, like_count, comment_count, lecture_activity_id, user_id, lecture_id) VALUES (2, 2, 2, 2, 2, 2);
INSERT INTO lecture_activity (view_count, like_count, comment_count, lecture_activity_id, user_id, lecture_id) VALUES (3, 3, 3, 3, 3, 3);

SELECT * FROM lecture_activity;


UPDATE users
SET
    data = {"role": 'student', "date_registered": '2019-10-20'},
	email = 'test5@mail.com'
WHERE user_id = 1 IF EXISTS;

SELECT * FROM users;

UPDATE users
SET
	subjects = {2, 3}
WHERE user_id = 2 IF EXISTS;

SELECT * FROM users;

UPDATE users
SET
	email = 'test7@mail.com'
WHERE user_id = 3 IF EXISTS;

SELECT * FROM users;

UPDATE groups
SET
	user_email = 'test8@mail.com'
WHERE group_id = 1 and user_id = 1 and group_name = 'km-61' IF EXISTS;

SELECT * FROM groups;

UPDATE groups
SET
	user_email = 'test10@mail.com'
WHERE group_id = 2 and user_id = 2 and group_name = 'km-62' IF EXISTS;

SELECT * FROM groups;

UPDATE groups
SET
	user_email = 'test11@mail.com'
WHERE group_id = 3 and user_id = 3 and group_name = 'km-63' IF EXISTS;

SELECT * FROM groups;


UPDATE subjects
SET
	name = 'name1'
WHERE lecture_id = 1 and subject_id = 1 and group_id = 1 IF EXISTS;

SELECT * FROM subjects;

UPDATE subjects
SET
	users = {1}
WHERE lecture_id = 2 and subject_id = 2 and group_id = 2 IF EXISTS;

SELECT * FROM subjects;

UPDATE subjects
SET
	name = 'name1',
    users = {1, 2}
WHERE lecture_id = 3 and subject_id = 3 and group_id = 3 IF EXISTS;

SELECT * FROM subjects;


UPDATE lectures
SET
    modified = '2020-10-10'
WHERE lecture_id = 3 and version = 'v3' IF EXISTS;

UPDATE lectures
SET
    meta = {'tags': ['tag6']}
WHERE lecture_id = 1 and version = 'v1' IF EXISTS;

UPDATE lectures
SET
    modified = '2020-11-10',
    meta = {'tags': ['tag3', 'tag4', 'tag5', 'tag6']}
WHERE lecture_id = 3 and version = 'v3' IF EXISTS;

SELECT * FROM lectures;

UPDATE lecture_pack
SET
    pack_name = 'test123'
WHERE lecture_id = 1 and pack_id = 1 IF EXISTS;

UPDATE lecture_pack
SET
    pack_name = 'test124',
    description = 'test description'
WHERE lecture_id = 2 and pack_id = 2 IF EXISTS;

UPDATE lecture_pack
SET
    description = 'test description 123'
WHERE lecture_id = 3 and pack_id = 3 IF EXISTS;

SELECT * FROM lecture_pack;

UPDATE lecture_comment
SET
    text = 'comment'
WHERE lecture_id = 1 and comment_id = 1 IF EXISTS;

UPDATE lecture_comment
SET
    datetime = '2020-10-10',
    text = '123'
WHERE lecture_id = 2 and comment_id = 2 IF EXISTS;

UPDATE lecture_comment
SET
    text = 'comment',
    likes = 10
WHERE lecture_id = 3 and comment_id = 3 IF EXISTS;

SELECT * FROM lecture_comment;

UPDATE lecture_activity
SET
    view_count = 5
WHERE lecture_id = 1 and lecture_activity_id = 1 and user_id = 1 IF EXISTS;

UPDATE lecture_activity
SET
    view_count = 1,
    like_count = 10
WHERE lecture_id = 2 and lecture_activity_id = 2 and user_id = 2 IF EXISTS;

UPDATE lecture_activity
SET
    view_count = 15,
    like_count = 15,
    comment_count = 15
WHERE lecture_id = 3 and lecture_activity_id = 3 and user_id = 3 IF EXISTS;

SELECT * FROM lecture_activity;


select * from users where user_id = 1 allow filtering;
select * from groups where user_id = 1 allow filtering;
select * from subjects where group_id = 1 allow filtering;
select * from lectures where lecture_id = 1 allow filtering;



delete from users WHERE user_id = 1 IF EXISTS;
delete from users WHERE user_id = 2 IF EXISTS;
delete from users WHERE user_id = 3 IF EXISTS;

delete from groups WHERE group_id = 1 and user_id = 1 and group_name = 'km-61' IF EXISTS;
delete from groups WHERE group_id = 2 and user_id = 2 and group_name = 'km-62' IF EXISTS;
delete from groups WHERE group_id = 3 and user_id = 3 and group_name = 'km-63' IF EXISTS;

delete from subjects WHERE lecture_id = 1 and subject_id = 1 and group_id = 1 IF EXISTS;
delete from subjects WHERE lecture_id = 2 and subject_id = 2 and group_id = 2 IF EXISTS;
delete from subjects WHERE lecture_id = 3 and subject_id = 3 and group_id = 3 IF EXISTS;

delete from lectures WHERE lecture_id = 3 and version = 'v3' IF EXISTS;
delete from lectures WHERE lecture_id = 1 and version = 'v1' IF EXISTS;
delete from lectures WHERE lecture_id = 3 and version = 'v3' IF EXISTS;

delete from lecture_pack WHERE lecture_id = 1 and pack_id = 1 IF EXISTS;
delete from lecture_pack WHERE lecture_id = 2 and pack_id = 2 IF EXISTS;
delete from lecture_pack WHERE lecture_id = 3 and pack_id = 3 IF EXISTS;

delete from lecture_comment WHERE lecture_id = 1 and comment_id = 1 IF EXISTS;
delete from lecture_comment WHERE lecture_id = 2 and comment_id = 2 IF EXISTS;
delete from lecture_comment WHERE lecture_id = 3 and comment_id = 3 IF EXISTS;

delete from lecture_activity WHERE lecture_id = 1 and lecture_activity_id = 1 and user_id = 1 IF EXISTS;
delete from lecture_activity WHERE lecture_id = 2 and lecture_activity_id = 2 and user_id = 2 IF EXISTS;
delete from lecture_activity WHERE lecture_id = 3 and lecture_activity_id = 3 and user_id = 3 IF EXISTS;
