#!/usr/bin/node
import { list } from './100-data.js';
console.log(list.map((item, idx) => list * idx));
