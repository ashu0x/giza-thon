use orion::numbers::{FixedTrait, FP16x16};

fn compute(ref a: Array<FP16x16>) {
a.append(FP16x16 { mag: 58959, sign: false });
a.append(FP16x16 { mag: 13531, sign: true });
a.append(FP16x16 { mag: 7880, sign: false });
a.append(FP16x16 { mag: 3573, sign: false });
a.append(FP16x16 { mag: 4365, sign: true });
a.append(FP16x16 { mag: 7667, sign: false });
a.append(FP16x16 { mag: 2589, sign: false });
a.append(FP16x16 { mag: 1, sign: false });
}