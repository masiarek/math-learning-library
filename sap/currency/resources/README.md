# Resources: SAP Notes, help pages, books and articles

**Level:** reference · for everyone

**One line:** The reading list behind this chapter: the SAP Notes that define the behaviour, the help-portal pages that explain it, the book chapters that teach it, and the working notes that started it.

Notes and KBAs are reachable at `https://me.sap.com/notes/<number>` (S-user login) and, for KBAs, at `https://userapps.support.sap.com/sap/support/knowledge/en/<number>` without one. Numbers below were verified against SAP's own page titles or against pages that quote them; a handful of numbers that circulate in older documents (174193, 1332795, 2579584) could not be verified and are listed at the end.

## SAP Notes and KBAs

### The update currency and "only balances in local currency"

| Number | Title |
|---|---|
| 391532 | Update currency in line items |
| 20054 | Clearing of foreign currency documents in local currency |
| 2249505 | "No forex rate diff. if clear in LC" Scope (T001-XSLTA) |
| 2220851 | Clearing local curr. Flowchart: How to avoid F5263 |
| 1697833, 1699746, 1701011 | F5063 / F5263 when clearing (F-03, FBB1, manual amounts) |
| 1904331 | Customer can't clear open items even balance in local currency is zero in FAGLB03 or FS10N |
| 1906780 | Was unable to clear FI documents due to error F1806 (BSEG-PSWSL not set) |
| 3511670 | Transaction F.13 clears a single line item |
| 3595533 | DF05B-PSBET was not recalculated during clearing in F-03 |
| 3651272 | ACDOCA-RTCUR is updated incorrectly with LC |
| 2219419 | FB03 incorrect foreign currency amount (PSWSL/PSWBT display) |
| 2393152 | Unexpected system behavior when changing flag "Only balances in local crcy" (SKB1-XSALH) for P&L accounts |
| 3057269 | No foreign currency balances are carried forward (XSALH) |
| 3423090 | Error FH085 "Account still has balance" when changing "Only balances in local currency" |
| 3270987 | "Balances for reconciliation accounts only in local currency not defined" when changing a reconciliation account |
| 1858966 | FAGL_SWITCH_OP092 error in FAGL_ACTIVATE_OP (XSALH history) |
| 2888262 | Currency & not permitted in account & / & |

### Exchange rate differences on clearing

| Number | Title |
|---|---|
| 2560929 | Guided Answer: exchange rate difference issue when clearing in FI |
| 2547111 | Unexplained exchange rate difference when clearing open item |
| 2374210 | Exchange rate difference at clearing versus asterisk |
| 1796941 | FBRA: option "Only resetting" is not allowed when exchange rate difference is posted |
| 3677911 | Reset Cleared Items app: reset restricted due to foreign exchange rate difference (Cloud) |
| 3619218 | Activating/deactivating forex gain and loss during clearing in local currency (Cloud) |
| 1920513 | Exchange rate postings after bank statement processing for assigned payments |
| 1523296 | FAGL_FC_VAL, FAGL_FCV and SAPF100 account determination KDB or KDF |
| 3430423 | OBA1 Define Accounts for Exchange Rate Differences: transport is disabled |

### Foreign currency valuation and translation

| Number | Title |
|---|---|
| 2312235 | FAGL_FCV delta logic: cleared items are evaluated regardless of the valuation selection |
| 3502546 | Reversal of valuation postings is possible after activation of delta logic |
| 3641501 | Clarification on delta logic behavior in FAGL_FCV for open item valuation |
| 3715580 | Year-end or mid-year valuation not permitted for vendor/customer open items (delta logic) |
| 3310524 | Posting period not open for variant and ledger for delta logic valuation |
| 2895010 | Difference in company code currency amounts during foreign currency valuation reset |
| 3127556 | How to reset foreign currency valuation (Cloud) |
| 2443070, 3359366, 3618871 | Exchange rate / rate type used by the valuation differs from OB08 |
| 3018508 | FAGL_FCV: header "Exchange rate" / "Translation date" initial in the valuation documents |
| 3018485, 3691303 | Valuate foreign currency open items on the GR/IR account |
| 2733138 | FAGL_FC_VAL / FAGL_FCV unexpectedly reads T030S |
| 3320183 | Group currency is not valuated by "Foreign Currency Valuation" |
| 3138607 | No valuation takes place (XSALH, open item management) |
| 1910482 | Valuation loss and revenue posted per account instead of netted |
| 3121140 | Foreign currency valuation posting gain or loss account determination |
| 1714718, 2561409 | Valuation with hedged exchange rate / exchange hedging for balance sheet accounts |
| 3321223 | T044A-XPOSD still exists but is not available in OB59 |
| 2155605 | Improving performance for foreign currency valuation programs |
| 3503527, 3425124, 3526213 | Advanced foreign currency valuation: currency concept, document type, account after clearing (Cloud) |
| 2059254 | FAGL_FC_TRANS: reset doesn't generate postings |
| 2431662 | FAGL_FC_TRANS: additional characteristics not considered |
| 3154025 | Specifying a source currency type in FAGL_FC_TRANS |
| 3582037 | Error FR884 in FAGL_FC_TRANS (OBA1 account determination) |
| 2441607, 2720369 | EWCT exchange rates |

### Exchange rates and rate types

| Number | Title |
|---|---|
| 1848683 | Translation date (BKPF-WWERT) derivation in Financial Accounting |
| 2646229 | Amount in local currency is not converted correctly as per OB08 settings |
| 2359878 | Exchange rate is not reflected in BKPF-KURSF correctly |
| 3107891 | Incorrect currency exchange rates (inverse rates, transactional data) |
| 3366043, 3314213 | Exchange rate ratio in TCURF; ratio not updated in TCURR |
| 3363756 | Exchange rates in OB08 are displayed in red |
| 2455178 | OB08: prompt for Customizing request unwanted |
| 3323804 | Direct and indirect quotation, SSCUI "Define Standard Quotation for Exchange Rates" |
| 2894303 | Exchange rate pair is not maintained: direct quotation (Cloud) |
| 3459075 | "A different quotation method has been defined for this currency pair" in the Currency Exchange Rates app |
| 3155262, 3280826 | Import Foreign Exchange Rates with indirect quotation |
| 3146374 | Exchange rate type with 6 decimal places |
| 2542937 | Understanding the currency conversion settings in FINSC_LEDGER |
| 2919967 | Assignment of exchange rate type and translation date type in currency conversion settings (Cloud) |
| 1700266 | Change exchange rate type in OB22 / FINSC_LEDGER |
| 3512760 | Different exchange rate type per ledger not possible (Cloud) |
| 2592703 | Exchange rate type in OBA7 not used in goods receipts |
| 2549273 | Pricing exchange rate not derived by the expected rate type in SD |
| 3062527 | Accrual engine: derivation of exchange rates and rate types |
| 3438847 | Alternative exchange rate type in F111 |
| 3700192 | Exchange rate determination using BAdI (Cloud) |
| 2806563 | KSII object currency uses a different exchange rate date |
| 3693632 | "Company Code Currency Determination Method" and exchange rates on journal entry items (Cloud) |
| 2619405 | Market data upload |

### Currency keys and decimal places

| Number | Title |
|---|---|
| 137626 | FAQ: Decimal places for currency codes |
| 1240163 | Amount too high by factor of 100 for HUF, JPY currencies |
| 3369259 | Change decimal places for a currency code |
| 2776679 | Change currency number of decimals for posted transactions |
| 3556933 | Not able to configure 2 decimals for currencies (TWD, IDR) |
| 3517123 | Migration cockpit template allows zero or two but not three decimal places |
| 2920613 | Enter a number with no decimal places |
| 2743937 | ME21N: decimal places are not permitted (message 00011) |
| 2603405 | Decimal places in ANEP/ANLC for JPY or TWD |
| 2710535 | Two decimal places assigned to controlling area currency in COEP (SE16) |
| 2123695 | Currency conversion incorrect by a factor of 100 in HANA Studio |
| 2973787 | Conversion of decimal places for currencies in custom logic (Cloud) |
| 2169454 | Rounding difference in artificial currency |
| 1679279 | Wrong decimal places displayed for price fields |
| 2250861 | Is it possible to change the default decimal notation for currencies? |
| 1646349 | Decimal shift in user currency fields |

### Universal Journal, ledgers and currency types

| Number | Title |
|---|---|
| 2344012 | Currencies in Universal Journal |
| 2334583 | Introduction of new currencies and currency types in SAP S/4HANA |
| 3015594 | FAQ: SAP S/4HANA ledger and currency Customizing (transaction FINSC_LEDGER) |
| 2543240 | FINSC_LEDGER: FINS_ACDOC_CUST242 (freely defined type cannot be an FI currency) |
| 2446407, 3009909 | Currency type 30 cannot be assigned / is missing for the global currency |
| 2810569 | FINS_ACDOC_CUST298 with FINSC_LEDGER |
| 2895413, 3253173 | Currency conversion settings cannot be saved in FINSC_LEDGER |
| 3485630 | Currency type cannot be changed on non-leading ledgers after shell conversion |
| 3548366 | Currency key is not editable for standard currency types in FINSC_LEDGER |
| 3622052 | Functional currency is not visible in FINSC_LEDGER |
| 3706725 | Assign consistent group currency types to company codes relevant for group reporting (FINS_ACDOC_CUST516) |
| 2593455 | Trial balance report for freely defined currency types |
| 2931078 | FAGLF101 returns FINS_ACDOC_UTIL023 (freely defined currency types) |
| 2856805 | Cannot create additional currency (freely defined currency, Cloud) |
| 2270333, 2270339 | S4TWL: data model changes in FIN; General Ledger |

### Universal Parallel Accounting

| Number | Title |
|---|---|
| 3191636 | Universal Parallel Accounting: scope information |
| 3265275 | Universal Parallel Accounting: FAQ |
| 3327778 | Migration to Universal Parallel Accounting (S/4HANA 2023): scope information |
| 3577390 | Activation of Universal Parallel Accounting |
| 3419623 | Restriction for profit center valuation |

### Material Ledger, Controlling and CO-PA

| Number | Title |
|---|---|
| 2396864 | Material Ledger obligatory for material valuation in S/4HANA |
| 3305451 | Central KBA for Material Ledger |
| 2555648 | No new currency types can be added or modified once the ML is active |
| 2453275, 2426246, 2429640, 3335505 | OMX2 / OMX3 currency type errors (C+339, KM133, MLCCS003) |
| 2427356, 2486551 | OMX1 ML type errors |
| 2570770 | CL_FML_ML_CURRENCY_CHECK dump / FINS_ACDOC_CUST028 |
| 3246781 | CKMLCT with different currency types per valuation area |
| 2681167 | Currency translation rules in the Material Ledger |
| 1511335 | C+039 ML currencies are changed in CO |
| 2530890 | Material Ledger with actual costing in S/4HANA 1709 |
| 2420690, 2156037, 3367502 | Goods receipts in legal, group and parallel valuation from affiliated companies |
| 1920994 | Actual price calculation in parallel currencies (CKM3) |
| 2161317 | Exchange rate type in product costing |
| 2506193 | Sales order price for group currency (CK51N) |
| 3513568 | Cost estimate with inconsistent values between company code and controlling area currency |
| 1754054 | MR21/MR22: incomplete price change with multiple currencies |
| 3062950 | Difference between company code currency and group currency (price unit rounding) |
| 2356348 | Display in company code currency by default with cost analysis |
| 3300701 | Object / transaction currency does not balance to zero after allocation |
| 3363959 | Changing currency on internal order (KO288) |
| 2547586 | Plan price in a different currency in KP26 |
| 3529726 | Default currency setting for base planning objects |
| 3013212 | Currency exchange rate in Manage Cost Rates - Actual (Cloud) |
| 553626 and 2182929, 2221237, 2322447, 2559609, 2718989 | FAQ Profitability Analysis, parts I–VI |
| 2276469 | Group currency in CO-PA (record type F) |
| 1887480 | Foreign currency key not transferred to CO-PA from FI posting |
| 2412947 | Currency translation in KE30 |
| 3337760 | KE28 / KE28L log showing only B0 currency |
| 2667649 | FAQ on CO-PA issues (Cloud) |

### Group reporting

| Number | Title |
|---|---|
| 3258768 | Currency translation errors in group reporting |
| 3137945 | Translation key 6 posts with CT indicator 1 and 4 |
| 3524961 | Currency translation posts the default partner unit |
| 3756349 | "Debit difference item is not included in the item group" when saving a translation method |
| 3146025 | Different amount in LC and GC with the same currency in reported data |
| 3501827 | Cross exchange rate / reference currency in group reporting |
| 3521168 | Group currency is not directly converted from transaction currency (TC → LC → GC) |
| 3506058 | Transaction and group currency match but amounts differ |
| 3492731 | FAQ on currency translation in HANA Cloud |

### Currency changeover and new currencies

| Number | Title |
|---|---|
| 3093354 | Collective note for euro changeover in Croatia |
| 3251724 | Euro currency changeover for Croatia (EWUCSIZE dump) |
| 3642962 | Sync ACDOCA/ACDOCU data with ICADOCM after local currency changeover |
| 2623984, 2626145 | Currency change and hyperinflation in Venezuela |
| 3484778 | ZWG, Zimbabwe Gold (ISO 4217 amendment 177) |
| 3559059 | Currency XCG for Sint Maarten and Curaçao (Ariba) |
| 123298 | Euro: conversion of document currency in sales and distribution |

### ABAP, BAPIs and the amount field length

| Number | Title |
|---|---|
| 2659445 | Usage of BAPI_CURRENCY_CONV_TO_INTERNAL and BAPI_CURRENCY_CONV_TO_EXTERNAL |
| 3473266 | Incorrect currency conversion by CONVERT_TO_LOCAL_CURRENCY (decimal precision) |
| 3408754 | Exchange rate determination in SAP TM with enhancement possibilities |
| 1656732 | Rounding in condition value when the condition has a different currency |
| 2628654 | S4TWL: Amount Field Length Extension |
| 2610650 | Amount Field Length Extension: code adaptations |
| 2601956 | Amount Field Length Extension: restriction note |
| 3509051, 3584195, 3613316 | Amounts with more than 13 digits; AFLE007 in BAPI_ACC_DOCUMENT_POST and the migration cockpit |
| 1973529 | KWERT and KBETR field length (V1802) |
| 2800818 | S/4HANA 1909 release information note for Finance |

### Not verified

174193 (*Update currency in line items*, cited beside 391532 in older documents), 1332795 (*Reconciliation account category "V": only balances in local currency*), 2579584 (CDS-based analytics, cited in SAP Note 2344012), 2422457, 3325920, 3443265, 619330, 2410560. They may well exist; check in SAP for Me before citing.

## SAP Help Portal and support content

- [Update currency (BSEG-PSWSL) in FI document line item ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361880798.html)
- [Update currency (BSEG-PSWSL) in exchange rate difference line item ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361878966.html)
- [How the logic of the GL update currency amount (BSEG-PSWBT) works in General Ledger ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361880924.html)
- [Indicator: "Only Manage Balances in Local Currency" (SKB1-XSALH) ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361878121.html)
- [Indicator: "No forex rate diff. when clearing in LC" (T001-XSLTA) ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361878929.html)
- [Exchange rate types, exchange rates and translation ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361878126.html)
- [Possible reasons for (huge) exchange rate differences ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361880873.html)
- [FAGL_FC_VAL: delta logic foreign currency valuation ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361878651.html)
- [Account determination in SAPF100, FAGL_FC_VAL and FAGL_FCV ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361880543.html)
- [Most common errors in FAGL_FC_VAL and FAGL_FCV ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361879058.html)
- [Foreign currency valuation for the WRX GR/IR clearing account ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361880193.html)
- [Foreign currency translation, Financial Accounting ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361878715.html)
- [About the foreign currency translation tool (EWCT) ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361880890.html)
- [SFIN: Define Settings for Ledgers and Currency Types ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361879104.html)
- [Manually entered local currency amount of a parked document is overwritten during posting ↗](https://help.sap.com/docs/SUPPORT_CONTENT/fiaccounting/3361880275.html)
- [Calculation of exchange rate in Profitability Analysis ↗](https://help.sap.com/docs/SUPPORT_CONTENT/ficontrolling/3361880544.html)
- [Overview of important tables used for currency translation (TCUR*) ↗](https://help.sap.com/docs/SUPPORT_CONTENT/bwplaolap/3361385803.html)
- [Amount Field Length Extension (S/4HANA product assistance) ↗](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/888cbe952a0e4a729f8b823d69860929/79ab49f06ec54874b00e5f6cf10d4fe0.html)
- [SAP S/4HANA, currency changeover add-on ↗](https://help.sap.com/docs/S4_CURRENCY_CHANGEOVER)
- [Universal Parallel Accounting (product assistance) ↗](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/09d5264e467d4491a82a32335a52e45f/9dcffed7a95741f9abe0db8bfd8a7f81.html) and the [UPA guide for S/4HANA 2023 (PDF) ↗](https://help.sap.com/doc/d078f3c7e8724bb283e30298f5ae422f/2023.0_UPA/en-US/88d56705fac34577992614b5509e7e91.pdf)
- [Ledger group ↗](https://help.sap.com/docs/sap_s4hana_on-premise/651d8af3ea974ad1a4d74449122c620e/ac37c753b1081d4be10000000a174cb4.html), [Portrayal using parallel ledgers ↗](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/f94fd7531a4d424de10000000a174cb4.html), [Extension ledger ↗](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/f2a1f5756fa148c8ae8ec338a2653fad.html)
- [Advanced foreign currency valuation ↗](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/651d8af3ea974ad1a4d74449122c620e/e3f896e4b0af4d1dbf00420e268221b0.html)
- [Direct and indirect quotation for exchange rates ↗](https://help.sap.com/docs/BS_CA/81601232c0824e84b4f5273f9acde9cf/aec38d5377a0ec23e10000000a174cb4.html)
- [Import Foreign Exchange Rates (S/4HANA Cloud) ↗](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/103f7a57015b8a1be10000000a44147b.html) and [Currencies (S/4HANA Cloud) ↗](https://help.sap.com/docs/SAP_S4HANA_CLOUD/0fa84c9d9c634132b7c4abb9ffdd8f06/f22f2aca75404b5f84becb9b246023b2.html)
- [Currency translation, group reporting ↗](https://help.sap.com/docs/SAP_S4HANA_CLOUD/90c07e91c7a64f328be3fd6b48955b13/71f7814e0cfc4ebbaaded46b6237a58d.html)
- [Specifying the controlling area currency ↗](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/f641de531ed3424de10000000a174cb4.html), [Operating concern ↗](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/5e23dc8fe9be4fd496f8ab556667ea05/dc07ad531e332f56e10000000a4450e5.html)

## ABAP keyword documentation

- [Currency key (glossary) ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/ABENCURRENCY_KEY_GLOSRY.html), [DDIC currency field (glossary) ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/ABENDDIC_CURRENCY_FIELD_GLOSRY.html), [ABAP CDS amount field (glossary) ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/ABENCDS_AMOUNT_FIELD_GLOSRY.html)
- [DDIC currency fields ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/abenddic_currency_field.htm) and [built-in DDIC types ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/abenddic_builtin_types.htm)
- [Semantics.amount.currencyCode ↗](https://help.sap.com/doc/abapdocu_cp_index_htm/CLOUD/en-US/ABENCDS_689127610-_ANNO.html)
- [CDS conversion functions: currency and unit ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/abencds_conv_func_unit_curr_v2.htm) (view entities) and [the DDIC-based view variant with DECIMAL_SHIFT ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/abencds_conv_func_unit_curr_v1.htm)
- [ABAP SQL: CURRENCY_CONVERSION and UNIT_CONVERSION ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/abensql_curr_unit_conv_func.htm)
- [WRITE: CURRENCY, DECIMALS, ROUND ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/abapwrite_int_options.htm), [WRITE TO format options ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-us/abapwrite_to_options.htm), [string template format options ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-us/abapcompute_string_format_options.htm)
- [round( ) and the decimal floating point functions ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-us/abendec_floating_point_functions.htm), [SET COUNTRY ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/abapset_country.htm)
- [Selecting the numeric type ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/abenselect_numeric_type_guidl.htm) and [rounding errors ↗](https://help.sap.com/doc/abapdocu_latest_index_htm/latest/en-US/abenrounding_error_guidl.htm) (programming guidelines)
- SAP samples: [cloud-abap-exchange-rates ↗](https://github.com/SAP-samples/cloud-abap-exchange-rates) (loads ECB rates through CL_EXCHANGE_RATES) and the [ABAP cheat sheets ↗](https://github.com/SAP-samples/abap-cheat-sheets/blob/main/03_ABAP_SQL.md)

## Books

Chapters that deal with currencies, from the publishers' tables of contents. SAP PRESS titles are at sap-press.com; editions change, so look for the current one.

| Title | Author(s), publisher | Where the currencies are |
|---|---|---|
| *Financial Accounting in SAP S/4HANA: Business User Guide* | Tritschler, Walz, Rupp, Mucka · SAP PRESS | General ledger master data and the currency fields of a journal entry; foreign currency valuation and regrouping in the closing chapter |
| *Configuring SAP S/4HANA Finance* | Pougkas · SAP PRESS | Organizational structure (company code, currencies), ledgers and currency types (FINSC_LEDGER), exchange rates, foreign currency valuation |
| *SAP S/4HANA Finance: The Reference Guide to What's New* | Salmon, Haesendonckx · SAP PRESS | The Universal Journal and its currencies; parallel accounting; UPA in the later edition |
| *Controlling with SAP S/4HANA: Business User Guide* | Salmon, Walz · SAP PRESS | Controlling area currency, object currency, transfer prices and group valuation |
| *Material Ledger in SAP S/4HANA* and *Actual Costing with the SAP Material Ledger* | Ovigele and others · SAP PRESS | ML currency types (OMX2/OMX3), parallel valuation, actual costing per currency |
| *Group Reporting with SAP S/4HANA* | Ryan, Ulrich and others · SAP PRESS | Currency translation methods, exchange rate indicators, translation differences |
| *SAP Foreign Currency Revaluation: FAS 52 and GAAP Requirements* | Finke · Wiley | The one book devoted entirely to valuation: methods, account determination, the accounting behind it |
| *New General Ledger in SAP ERP Financials* | Bauer, Siebert · SAP PRESS | The new G/L's parallel currencies per ledger, the ancestor of FINSC_LEDGER |
| *Core Data Services for ABAP* | Colle, Dentzer, Hrastnik · SAP PRESS | Amount and currency annotations, currency conversion in views |
| Introductory ABAP texts (*Getting Started with ABAP*, *ABAP: An Introduction*, and their predecessors) | SAP PRESS | The CURRENCY addition on WRITE and the Dictionary reference field |

## Blogs and community articles

- [SAP S/4HANA currency setup ↗](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-currency-setup/ba-p/13379639) (SAP blog; the canonical walk-through of FINSC_LEDGER)
- [SAP S/4HANA controlling area currency type setup ↗](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/sap-s-4hana-controlling-area-currency-type-setup/ba-p/13528570)
- [Currencies in a live S/4HANA Finance 1809 environment ↗](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-members/currencies-in-a-live-s-4hana-finance-1809-environment/ba-p/13366125)
- [Defining currency types for the general ledger in SAP S/4HANA ↗](https://blog.sap-press.com/defining-currency-types-for-the-general-ledger-in-sap-s4hana) and [Working with group currency in SAP S/4HANA ↗](https://blog.sap-press.com/working-with-group-currency-in-sap-s4hana) (SAP PRESS blog)
- [Universal Parallel Accounting in SAP S/4HANA ↗](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/universal-parallel-accounting-in-sap-s-4hana/ba-p/13551060), [Readiness for Universal Parallel Accounting ↗](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/readiness-for-universal-parallel-accounting/ba-p/13635682), [UPA limitations and opportunities ↗](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-members/universal-parallel-accounting-limitations-and-opportunities/ba-p/14072763)
- [Understanding the currency translation process in SAP S/4HANA Finance for group reporting ↗](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/understanding-currency-translation-process-in-sap-s-4hana-finance-for-group/ba-p/13457526)
- [Transfer prices in Material Ledger: currencies, ledgers and multiple valuations ↗](https://blogs.sap.com/2023/02/06/transfer-prices-in-material-ledger-currencies-ledgers-and-multiple-valuations/)
- [How to maintain exchange rates in SAP S/4HANA Cloud ↗](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/how-to-maintain-exchange-rates-in-sap-s-4hana-cloud/ba-p/12844623) and [Bring your own rates to SAP Market Rates Management ↗](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/bring-your-own-rates-to-sap-market-rates-management-in-3-easy-steps/ba-p/13404009)
- [Amount Field Length Extension (AFLE) limitations in SAP S/4HANA ↗](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/amount-field-length-extension-afle-limitations-in-sap-s-4-hana/ba-p/13444049)
- [Currency changeover needs on productive SAP S/4HANA on-prem and private cloud ↗](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/currency-changeover-needs-on-productive-sap-s-4-hana-on-prem-and-private/ba-p/14155317)
- [ABAP CDS cheat sheet: amounts and quantities in ABAP CDS ↗](https://community.sap.com/t5/technology-blog-posts-by-sap/abap-cds-cheat-sheet-amounts-and-quantities-in-abap-cds/ba-p/13542627) and [New currency conversion function in ABAP SQL ↗](https://community.sap.com/t5/application-development-and-automation-blog-posts/new-currency-conversion-function-in-abap-sql/ba-p/13501087)
- [Nine tips for dealing with zero decimal place currencies ↗](https://sapinsider.org/nine-tips-for-dealing-with-zero-decimal-place-currencies/) and [Currency decimal issue: JPY, KRW, VND ↗](https://community.sap.com/t5/application-development-and-automation-blog-posts/currency-decimal-issue-jpy-krw-vnd-localization-rollout-japan-korea-vietnam/ba-p/13416438)
- [Demystifying the ledger, currency setup and currency conversion in SAP S/4HANA Finance 1610 ↗](https://sapinsider.org/demystifying-the-ledger-currency-setup-and-currency-conversion-in-sap-s-4hana-finance-1610/) and [Managing currencies in a live SAP S/4HANA Finance 1809 environment ↗](https://sapinsider.org/blogs/managing-currencies-in-a-live-sap-s-4hana-finance-1809-environment/)

## The working documents this chapter grew out of

A set of Google Docs on multicurrency architecture, kept by the author of this library. They are the source of the worked examples and of several of the pages:

- Multicurrency Architecture, main document, with sub-documents on multi-currency accounting (MCA), the functional currency, the PSWSL / WAERS / DMBTR / DMBE3 fields and the update currency, currency types and real-time currency conversion, foreign currency valuation, inventory valuation with the Material Ledger, parallel accounting and parallel valuation, IFRS / US GAAP / local GAAP, asset accounting and production and overhead accounting under Universal Parallel Accounting, error correction and suspense accounting (ECS), parallel currencies for product costing, currency exchange rates in SAP S/4HANA, FINSC_LEDGER and the leading, non-leading and extension ledgers, and currency management in payments.
- *Indicator: "Only Manage Balances in Local Currency" (SKB1-XSALH)*, the document with the JPY screenshots that [its page](../only_balances_in_local_currency/README.md) reproduces.

Back to the chapter map: [Currencies in SAP](../README.md).
