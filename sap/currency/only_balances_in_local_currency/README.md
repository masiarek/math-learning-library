# "Only manage balances in local currency" (SKB1-XSALH)

**Level:** 301 · for FI consultants configuring G/L accounts with open item management

**One line:** One checkbox on the G/L master decides whether an open item posted in USD is remembered as USD or only as its yen equivalent — and therefore whether clearing it later at a different rate produces an exchange rate difference or nothing at all.

!!! note "Stub"
    This page is a placeholder in the currency chapter. The sections below name what it will cover; the content is being written page by page.

## What this page will cover

- What the indicator does: balances updated in local currency only, PSWSL = local currency
- Where it must be set (cash discount clearing, GR/IR), where it cannot (reconciliation accounts), and where it is optional
- The worked example: JPY company code, USD open item at 1 : 100, cleared at 1 : 110, with the flag on and off
- How the flag changes clearing: recalculated DMBTR, residual items, charge-off and the exchange rate difference line
- T001-XSLTA, "No forex rate diff. when clearing in LC", and how it interacts with the flag
- Changing the flag on an account that already has balances
- A program that replays both clearings and shows the 1,000 JPY difference

## Related pages

- [Update currency: BSEG-PSWSL and BSEG-PSWBT](../update_currency_pswsl/README.md)
- [Exchange rate differences on clearing (realized gains and losses)](../exchange_rate_differences_on_clearing/README.md)
- [Foreign currency valuation and translation (unrealized differences)](../foreign_currency_valuation/README.md)
- [Reporting and troubleshooting currency questions](../reporting_and_troubleshooting/README.md)

Back to the chapter map: [Currencies in SAP](../README.md).
