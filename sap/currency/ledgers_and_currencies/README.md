# Ledgers and their currencies: FINSC_LEDGER

**Level:** 201 · for FI consultants setting up S/4HANA

**One line:** In S/4HANA the ledger and its currencies are one configuration object: each ledger, per company code, lists the currency types it carries and how each is converted — so a non-leading ledger can add a currency but never drop one the leading ledger has in BSEG.

!!! note "Stub"
    This page is a placeholder in the currency chapter. The sections below name what it will cover; the content is being written page by page.

## What this page will cover

- Leading ledger 0L, non-leading standard ledgers and extension ledgers, and which of them can have their own currencies
- FINSC_LEDGER: the view cluster, the company code assignment, and the currency conversion settings per currency type
- Conversion settings: source currency type, exchange rate type, translation date type, and real-time versus period-end
- Ledger groups, accounting principles and the representative ledger
- ECC ancestry: T881, T882G, OB22 and what the migration carries over
- Fiscal year variants, posting periods and currencies per ledger: what may differ and what may not
- Extension ledgers and the currencies they inherit from their underlying ledger

## Related pages

- [Currencies in the Universal Journal (ACDOCA)](../universal_journal_currencies/README.md)
- [Local currency and the parallel currencies of a company code](../local_and_parallel_currencies/README.md)
- [Currency types: 00, 10, 30, 40, 50, 60 and the Z types](../currency_types/README.md)
- [Universal Parallel Accounting and currencies](../universal_parallel_accounting/README.md)
- [Foreign currency valuation and translation (unrealized differences)](../foreign_currency_valuation/README.md)

Back to the chapter map: [Currencies in SAP](../README.md).
