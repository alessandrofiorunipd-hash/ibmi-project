**free
ctl-opt dftactgrp(*no) actgrp(*new) option(*srcstmt);

/copy qrpglesrc/customer_h.rpgleinc

dcl-pr CusServ extpgm('CUSSERV');
  action char(10) const;
  customer likeds(Customer_t);
  success ind;
  errorMsg varchar(100);
end-pr;

dcl-ds testCust likeds(Customer_t);
dcl-s success ind;
dcl-s errorMsg varchar(100);
dcl-s failCount int(10) inz(0);

// --- Test Case 1: Missing Name ---
testCust = *allx'00';
testCust.name = '';
testCust.email = 'test@test.com';

CusServ('REGISTER' : testCust : success : errorMsg);

if success or errorMsg <> 'Customer name is required.';
  snd-msg 'TEST FAIL: Expected failure for missing name.';
  failCount += 1;
endif;

// --- Test Case 2: Invalid Email ---
testCust.name = 'Valid Name';
testCust.email = 'invalid-email';

CusServ('REGISTER' : testCust : success : errorMsg);

if success or errorMsg <> 'Invalid email address.';
  snd-msg 'TEST FAIL: Expected failure for invalid email.';
  failCount += 1;
endif;

// --- Summary ---
if failCount = 0;
  snd-msg 'ALL TESTS PASSED: CusServ';
else;
  snd-msg ('TEST SUITE FAILED: ' + %char(failCount) + ' errors.');
endif;

*inlr = *on;
