CREATE FUNCTION DeleteOldRowBlacklist() RETURNS trigger
    LANGUAGE PLPGSQL
    AS $$
BEGIN
  DELETE FROM public.blacklist WHERE "time_stamp" < NOW() - INTERVAL '14 days';
  RETURN NULL;
END;
$$;	



CREATE TRIGGER trigger_delete_old_rows
    BEFORE INSERT or update ON "blacklist"
    EXECUTE PROCEDURE DeleteOldRowBlacklist();




