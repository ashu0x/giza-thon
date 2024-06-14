use orion::numbers::{FixedTrait, FP16x16};

fn compute(ref a: Array<FP16x16>) {
a.append(FP16x16 { mag: 41852, sign: false });
a.append(FP16x16 { mag: 9551, sign: true });
a.append(FP16x16 { mag: 12816, sign: false });
a.append(FP16x16 { mag: 5018, sign: true });
a.append(FP16x16 { mag: 4198, sign: false });
a.append(FP16x16 { mag: 527, sign: false });
a.append(FP16x16 { mag: 199, sign: false });
a.append(FP16x16 { mag: 676, sign: false });
a.append(FP16x16 { mag: 1, sign: true });
a.append(FP16x16 { mag: 64, sign: false });
a.append(FP16x16 { mag: 3, sign: false });
a.append(FP16x16 { mag: 285, sign: false });
}