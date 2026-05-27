ALTER TABLE public.calculadora DROP COLUMN id;
ALTER TABLE public.calculadora ADD COLUMN id UUID DEFAULT gen_random_uuid();