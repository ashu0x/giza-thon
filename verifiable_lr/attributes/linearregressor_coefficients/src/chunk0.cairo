use orion::numbers::{FixedTrait, FP16x16};

fn compute(ref a: Array<FP16x16>) {
a.append(FP16x16 { mag: 33177, sign: false });
a.append(FP16x16 { mag: 7513, sign: false });
a.append(FP16x16 { mag: 2654, sign: false });
a.append(FP16x16 { mag: 4148, sign: false });
a.append(FP16x16 { mag: 5175, sign: false });
a.append(FP16x16 { mag: 262, sign: true });
a.append(FP16x16 { mag: 322, sign: true });
a.append(FP16x16 { mag: 0, sign: true });
}