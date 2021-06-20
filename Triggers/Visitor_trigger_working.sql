CREATE FUNCTION DeleteOldRowVisitor() RETURNS trigger
    LANGUAGE PLPGSQL
    AS $$
BEGIN
  DELETE FROM public.visitor_list WHERE "time_stamp" < NOW() - INTERVAL '10 days';
  RETURN NULL;
END;


CREATE TRIGGER trigger_delete_old_rows
    BEFORE INSERT or update ON "blacklist"
    EXECUTE PROCEDURE DeleteOldRowVisitor();



