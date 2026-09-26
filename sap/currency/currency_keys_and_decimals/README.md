# Currency keys, codes and decimal places

**Level:** 101 · for anyone who has typed a currency code into SAP

**One line:** A currency in SAP is a three-character key in TCURC, and the number of decimals it shows is a separate fact in TCURX — which is why 1,000 JPY is stored as 10.00 and why every amount field has to carry its key.

!!! note "Stub"
    This page is a placeholder in the currency chapter. The sections below name what it will cover; the content is being written page by page.

## What this page will cover

- ISO 4217 codes and the SAP currency key (TCURC, TCURT, OY03)
- Decimal places that are not two: TCURX and OY04, with JPY, KWD, CLP, HUF as the worked cases
- Internal versus external representation: what the database stores and what the screen shows
- Alternative currency keys, EMU membership, expired currencies and the special keys (USDN, EUR, XAU …)
- A program that shifts amounts between stored and displayed form and shows the classic ×100 bug

## Related pages

- [Rounding, rounding differences and the amount field](../rounding_and_amount_fields/README.md)
- [Currencies in ABAP: CURR, CUKY, CDS amount fields and conversion](../abap_currency_handling/README.md)
- [Exchange rates: TCURR, rate types, quotation and translation dates](../exchange_rates/README.md)
- [Introducing, changing and retiring currencies](../introducing_and_changing_currencies/README.md)

Back to the chapter map: [Currencies in SAP](../README.md).
