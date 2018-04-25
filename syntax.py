1st
# Syntax
    # SELECT
    # column_1,
    # aggregate_function (column_2)
    # FROM
    # table
    # GROUP BY
    # column_1
    # HAVING
    # search_condition;
2nd
To find albums that have the number of tracks between 18 and 20,
we refer to the aggregate function in the HAVING clause as the following statement:
    #SELECT
    #  albumid,
    #  COUNT(trackid)
    # FROM
    #  tracks
    # GROUP BY
    #  albumid
    # HAVING count(albumid) BETWEEN 18 AND 20
    # ORDER BY albumid;
3rd
The following statement queries data from tracks and albums tables using inner join
to find albums that have the total length greater than60,000,000 milliseconds.
    # SELECT
    #  tracks.albumid,
    #  title,
    #  sum(Milliseconds) AS length
    # FROM
    #  tracks
    # INNER JOIN albums ON albums.AlbumId = tracks.AlbumId
    # GROUP BY
    #  tracks.albumid
    # HAVING
    #  length > 60000000;
4th
    # SELECT
    # 	name,
    # 	milliseconds,
    # 	bytes,
    # 	albumid
    # FROM
    # 	tracks
    # WHERE
    # 	albumid = 1  //if albumid==1
    # AND milliseconds > 250000
    # AND name LIKE '%To%' // if "name" column contain "To"
    # AND albumid IN (2, 3, 4)      // if albumid is in (2,3,4) numbers
    All logical operators meaning
    # ALL	returns 1 if all expressions are 1.
    # AND	returns 1 if both expressions are 1, and 0 if one of the expressions is 0.
    # ANY	returns 1 if any one of a set of comparisons is 1.
    # BETWEEN	returns 1 if a value is within a range.
    # EXISTS	returns 1 if a subquery contains any rows.
    # IN	returns 1 if a value is in a list of values.
    # LIKE	returns 1 if a value matches a pattern
    # NOT	reverses the value of other operators such as NOT EXISTS, NOT IN, NOT BETWEEN, etc.
    # OR	returns true if either expression is 1