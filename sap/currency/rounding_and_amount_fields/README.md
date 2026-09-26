# Rounding, rounding differences and the amount field

**Level:** 201 · for developers and FI consultants

**One line:** Money in SAP is a packed decimal with the currency's decimal places, rounded commercially at every conversion, and a journal entry must balance to zero in *every* currency field — so the rounding difference is a real posting, not a display artefact.

!!! note "Stub"
    This page is a placeholder in the currency chapter. The sections below name what it will cover; the content is being written page by page.

## What this page will cover

- The amount field: packed decimal, 13 digits in ECC, 23 in S/4HANA (amount field length extension), and the CURR/CUKY pair
- Commercial rounding, rounding to the currency's decimals, and rounding rules per currency and company code (OB90, e.g. CHF 0.05)
- Balance zero per currency: why converting each line separately leaves a difference, and where it is posted
- Rounding differences in clearing, in tax, in the Material Ledger and in allocations
- Why float is the wrong type for money, and what Python's decimal module has in common with ABAP's packed numbers
- A program that converts a document line by line and shows the difference appear and get posted

## Related pages

- [Currency keys, codes and decimal places](../currency_keys_and_decimals/README.md)
- [Currencies in ABAP: CURR, CUKY, CDS amount fields and conversion](../abap_currency_handling/README.md)
- [Currencies in the Universal Journal (ACDOCA)](../universal_journal_currencies/README.md)
- [Exchange rates: TCURR, rate types, quotation and translation dates](../exchange_rates/README.md)

Back to the chapter map: [Currencies in SAP](../README.md).
