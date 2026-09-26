# Exchange rates: TCURR, rate types, quotation and translation dates

**Level:** 201 · for FI consultants and anyone who has been asked why a posting used the wrong rate

**One line:** An exchange rate in SAP is a row keyed by rate type, from-currency, to-currency and valid-from date, read backwards through inverse rates, ratios and a reference currency — so the rate a posting used is a derivation, not a lookup.

!!! note "Stub"
    This page is a placeholder in the currency chapter. The sections below name what it will cover; the content is being written page by page.

## What this page will cover

- Tables TCURR, TCURF, TCURV, TCURN, TCURW and the transactions OB08, OB07, OBBS, ONOT
- Exchange rate types M, G, B, P, EURX and what each is used for, plus custom types
- Direct and indirect quotation, the ratio factors and why 1 : 100 ratios exist
- Reference currency and cross rates, inverse rate, and the search order the system actually follows
- Translation date versus posting date versus document date: BKPF-KURSF, BKPF-WWERT and the rate stored on the document
- Rate tolerance warnings, fixed rates, and importing rates from a market data provider or a central bank
- A program that resolves a rate the way SAP does: ratio, inverse, reference currency, then conversion and rounding

## Related pages

- [Currency keys, codes and decimal places](../currency_keys_and_decimals/README.md)
- [Local currency and the parallel currencies of a company code](../local_and_parallel_currencies/README.md)
- [Foreign currency valuation and translation (unrealized differences)](../foreign_currency_valuation/README.md)
- [Exchange rate differences on clearing (realized gains and losses)](../exchange_rate_differences_on_clearing/README.md)
- [Currency management in payments and treasury](../payments_and_currency_management/README.md)

Back to the chapter map: [Currencies in SAP](../README.md).
