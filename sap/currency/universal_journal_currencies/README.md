# Currencies in the Universal Journal (ACDOCA)

**Level:** 301 · for anyone who has to read ACDOCA or plan an S/4HANA conversion

**One line:** ACDOCA carries up to thirteen amount fields per line — WSL, TSL, HSL, KSL, OSL … GSL and CO_OSL — each a currency *type* configured per ledger and company code, and only three of them survive into BSEG.

!!! note "Stub"
    This page is a placeholder in the currency chapter. The sections below name what it will cover; the content is being written page by page.

## What this page will cover

- The amount fields of ACDOCA and their currency key fields, mapped to BSEG and to the CO amount fields
- WSL versus TSL: document currency versus the currency the G/L balance is kept in
- Mandatory fields (WSL, TSL, HSL, KSL) and the eight freely defined fields
- BSEG-relevant currency types: the 1st/2nd/3rd FI currency and the rule for non-leading ledgers
- Real-time conversion in the accounting interface and balance zero per journal entry
- The process coverage matrix from SAP Note 2344012: which processes convert with historical rates and which fall back to the current rate
- Reporting on the non-BSEG currencies: FB03L, FAGLB03, FAGLL03H, the Fiori apps and CDS analytics
- A program that builds one journal entry in all currency fields and checks balance zero per field

## Related pages

- [Currency types: 00, 10, 30, 40, 50, 60 and the Z types](../currency_types/README.md)
- [Ledgers and their currencies: FINSC_LEDGER](../ledgers_and_currencies/README.md)
- [Universal Parallel Accounting and currencies](../universal_parallel_accounting/README.md)
- [Local currency and the parallel currencies of a company code](../local_and_parallel_currencies/README.md)
- [Update currency: BSEG-PSWSL and BSEG-PSWBT](../update_currency_pswsl/README.md)
- [Rounding, rounding differences and the amount field](../rounding_and_amount_fields/README.md)

Back to the chapter map: [Currencies in SAP](../README.md).
