# Currencies in ABAP: CURR, CUKY, CDS amount fields and conversion

**Level:** 201 · for ABAP developers

**One line:** An ABAP amount is never a number on its own: the Dictionary ties every CURR field to a CUKY field, CDS ties it with an annotation, and every output, conversion and comparison has to go through that link or the decimals of JPY and KWD will be wrong by a factor of 100 or 10.

!!! note "Stub"
    This page is a placeholder in the currency chapter. The sections below name what it will cover; the content is being written page by page.

## What this page will cover

- Dictionary types CURR and CUKY, the reference field and reference table, and the DDIC currency field glossary entries
- ABAP CDS amount fields: @Semantics.amount.currencyCode, @Semantics.currencyCode, and the built-in CURRENCY_CONVERSION function
- ABAP SQL: CURRENCY_CONVERSION and its parameters (exchange rate type, date, rounding, decimal shift, error handling)
- Output: WRITE … CURRENCY, string templates with CURRENCY =, DECIMALS, and the SET COUNTRY decimal separator
- Function modules: CONVERT_TO_LOCAL_CURRENCY, CONVERT_TO_FOREIGN_CURRENCY, READ_EXCHANGE_RATE, BAPI_CURRENCY_CONV_TO_INTERNAL / _EXTERNAL, BAPI_CURRENCY_GETDECIMALS, the CURRENCY_AMOUNT_* family
- The classic bugs: forgetting TCURX, multiplying by 100, using F or DECFLOAT without rounding, comparing amounts in different keys
- ABAP Cloud and RAP: released CDS views for currencies and exchange rates, and the APIs that replace direct table reads

## Related pages

- [Currency keys, codes and decimal places](../currency_keys_and_decimals/README.md)
- [Rounding, rounding differences and the amount field](../rounding_and_amount_fields/README.md)
- [Exchange rates: TCURR, rate types, quotation and translation dates](../exchange_rates/README.md)
- [Reporting and troubleshooting currency questions](../reporting_and_troubleshooting/README.md)

Back to the chapter map: [Currencies in SAP](../README.md).
