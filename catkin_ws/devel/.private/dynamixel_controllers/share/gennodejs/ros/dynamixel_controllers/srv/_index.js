
"use strict";

let SetComplianceMargin = require('./SetComplianceMargin.js')
let SetSpeed = require('./SetSpeed.js')
let SetCompliancePunch = require('./SetCompliancePunch.js')
let TorqueEnable = require('./TorqueEnable.js')
let SetTorqueLimit = require('./SetTorqueLimit.js')
let StopController = require('./StopController.js')
let StartController = require('./StartController.js')
let RestartController = require('./RestartController.js')
let SetComplianceSlope = require('./SetComplianceSlope.js')

module.exports = {
  SetComplianceMargin: SetComplianceMargin,
  SetSpeed: SetSpeed,
  SetCompliancePunch: SetCompliancePunch,
  TorqueEnable: TorqueEnable,
  SetTorqueLimit: SetTorqueLimit,
  StopController: StopController,
  StartController: StartController,
  RestartController: RestartController,
  SetComplianceSlope: SetComplianceSlope,
};
