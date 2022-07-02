import {
  Column,
  Entity,
  PrimaryGeneratedColumn,
  OneToMany,
  ManyToOne,
} from 'typeorm';

@Entity({ name: 'Final' })
export class Final {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: true })
  ten: string;

  @Column({ nullable: true })
  hang: string;

  @Column({ type: 'float', nullable: true })
  gia_moi: number;

  @Column({ type: 'float', nullable: true })
  kich_thuoc_man_hinh: number;

  @Column({ nullable: true })
  cong_nghe_man_hinh: string;

  @Column({ nullable: true })
  cpu: string;

  @Column({ type: 'float', nullable: true })
  ram: number;

  @Column({ type: 'float', nullable: true })
  bo_nho_trong: number;

  @Column({ nullable: true })
  pin: string;

  @Column({ nullable: true })
  sim: string;

  @OneToMany(() => FinalCellPhones, (finalCellPhones) => finalCellPhones.final)
  finalCellPhones: FinalCellPhones[];

  @OneToMany(() => FinalDidongviet, (finalDidongviet) => finalDidongviet.final)
  finalDidongviet: FinalDidongviet[];

  @OneToMany(
    () => FinalDienmayxanh,
    (finalDienmayxanh) => finalDienmayxanh.final,
  )
  finalDienmayxanh: FinalDienmayxanh[];

  @OneToMany(() => FinalTgdd, (finalTgdd) => finalTgdd.final)
  finalTgdd: FinalTgdd[];

  @OneToMany(() => FinalTiki, (finalTiki) => finalTiki.final)
  finalTiki: FinalTiki[];

  @OneToMany(() => FinalViettel, (finalViettel) => finalViettel.final)
  finalViettel: FinalViettel[];
}

@Entity({ name: 'CellPhones' })
export class CellPhones {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: true })
  ten: string;

  @Column({ type: 'float', nullable: true })
  gia_moi: number;

  @Column({ type: 'float', nullable: true })
  kich_thuoc_man_hinh: number;

  @Column({ nullable: true })
  cong_nghe_man_hinh: string;

  @Column({ nullable: true })
  cpu: string;

  @Column({ type: 'float', nullable: true })
  ram: number;

  @Column({ type: 'float', nullable: true })
  bo_nho_trong: number;

  @Column({ nullable: true })
  pin: string;

  @Column({ nullable: true })
  sim: string;

  @OneToMany(
    () => FinalCellPhones,
    (finalCellPhones) => finalCellPhones.cellPhones,
  )
  finalCellPhones: FinalCellPhones[];
}

@Entity({ name: 'Didongviet' })
export class Didongviet {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: true })
  ten: string;

  @Column({ type: 'float', nullable: true })
  gia_moi: number;

  @Column({ type: 'float', nullable: true })
  kich_thuoc_man_hinh: number;

  @Column({ nullable: true })
  cong_nghe_man_hinh: string;

  @Column({ nullable: true })
  cpu: string;

  @Column({ type: 'float', nullable: true })
  ram: number;

  @Column({ type: 'float', nullable: true })
  bo_nho_trong: number;

  @Column({ nullable: true })
  pin: string;

  @Column({ nullable: true })
  sim: string;

  @OneToMany(
    () => FinalDidongviet,
    (finalDidongviet) => finalDidongviet.didongviet,
  )
  finalDidongviet: FinalDidongviet[];
}

@Entity({ name: 'Dienmayxanh' })
export class Dienmayxanh {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: true })
  ten: string;

  @Column({ type: 'float', nullable: true })
  gia_moi: number;

  @Column({ type: 'float', nullable: true })
  kich_thuoc_man_hinh: number;

  @Column({ nullable: true })
  cong_nghe_man_hinh: string;

  @Column({ nullable: true })
  cpu: string;

  @Column({ type: 'float', nullable: true })
  ram: number;

  @Column({ type: 'float', nullable: true })
  bo_nho_trong: number;

  @Column({ nullable: true })
  pin: string;

  @Column({ nullable: true })
  sim: string;

  @OneToMany(
    () => FinalDienmayxanh,
    (finalDienmayxanh) => finalDienmayxanh.dienmayxanh,
  )
  finalDienmayxanh: FinalDienmayxanh[];
}

@Entity({ name: 'Tgdd' })
export class Tgdd {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: true })
  ten: string;

  @Column({ type: 'float', nullable: true })
  gia_moi: number;

  @Column({ type: 'float', nullable: true })
  kich_thuoc_man_hinh: number;

  @Column({ nullable: true })
  cong_nghe_man_hinh: string;

  @Column({ nullable: true })
  cpu: string;

  @Column({ type: 'float', nullable: true })
  ram: number;

  @Column({ type: 'float', nullable: true })
  bo_nho_trong: number;

  @Column({ nullable: true })
  pin: string;

  @Column({ nullable: true })
  sim: string;

  @OneToMany(() => FinalTgdd, (finalTgdd) => finalTgdd.tgdd)
  finalTgdd: FinalTgdd[];
}

@Entity({ name: 'Tiki' })
export class Tiki {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: true })
  ten: string;

  @Column({ type: 'float', nullable: true })
  gia_moi: number;

  @Column({ type: 'float', nullable: true })
  kich_thuoc_man_hinh: number;

  @Column({ nullable: true })
  cong_nghe_man_hinh: string;

  @Column({ nullable: true })
  cpu: string;

  @Column({ type: 'float', nullable: true })
  ram: number;

  @Column({ type: 'float', nullable: true })
  bo_nho_trong: number;

  @Column({ nullable: true })
  pin: string;

  @Column({ nullable: true })
  sim: string;

  @OneToMany(() => FinalTiki, (finalTiki) => finalTiki.tiki)
  finalTiki: FinalTiki[];
}

@Entity({ name: 'Viettel' })
export class Viettel {
  @PrimaryGeneratedColumn()
  id: number;

  @Column({ nullable: true })
  ten: string;

  @Column({ type: 'float', nullable: true })
  gia_moi: number;

  @Column({ type: 'float', nullable: true })
  kich_thuoc_man_hinh: number;

  @Column({ nullable: true })
  cong_nghe_man_hinh: string;

  @Column({ nullable: true })
  cpu: string;

  @Column({ type: 'float', nullable: true })
  ram: number;

  @Column({ type: 'float', nullable: true })
  bo_nho_trong: number;

  @Column({ nullable: true })
  pin: string;

  @Column({ nullable: true })
  sim: string;

  @OneToMany(() => FinalViettel, (finalViettel) => finalViettel.viettel)
  finalViettel: FinalViettel[];
}

@Entity({ name: 'Final_CellPhones' })
export class FinalCellPhones {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  finalId: number;

  @Column()
  cellPhonesId: number;

  @ManyToOne(() => Final, (final) => final.finalCellPhones)
  final: Final;

  @ManyToOne(() => CellPhones, (cellPhones) => cellPhones.finalCellPhones)
  cellPhones: CellPhones;
}

@Entity({ name: 'Final_Didongviet' })
export class FinalDidongviet {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  finalId: number;

  @Column()
  didongvietId: number;

  @ManyToOne(() => Final, (final) => final.finalCellPhones)
  final: Final;

  @ManyToOne(() => Didongviet, (didongviet) => didongviet.finalDidongviet)
  didongviet: Didongviet;
}

@Entity({ name: 'Final_Dienmayxanh' })
export class FinalDienmayxanh {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  finalId: number;

  @Column()
  dienmayxanhId: number;

  @ManyToOne(() => Final, (final) => final.finalCellPhones)
  final: Final;

  @ManyToOne(() => Dienmayxanh, (dienmayxanh) => dienmayxanh.finalDienmayxanh)
  dienmayxanh: Dienmayxanh;
}

@Entity({ name: 'Final_Tgdd' })
export class FinalTgdd {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  finalId: number;

  @Column()
  tgddId: number;

  @ManyToOne(() => Final, (final) => final.finalCellPhones)
  final: Final;

  @ManyToOne(() => Tgdd, (tgdd) => tgdd.finalTgdd)
  tgdd: Tgdd;
}

@Entity({ name: 'Final_Tiki' })
export class FinalTiki {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  finalId: number;

  @Column()
  tikiId: number;

  @ManyToOne(() => Final, (final) => final.finalCellPhones)
  final: Final;

  @ManyToOne(() => Tiki, (tiki) => tiki.finalTiki)
  tiki: Tiki;
}

@Entity({ name: 'Final_Viettel' })
export class FinalViettel {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  finalId: number;

  @Column()
  viettelId: number;

  @ManyToOne(() => Final, (final) => final.finalCellPhones)
  final: Final;

  @ManyToOne(() => Viettel, (viettel) => viettel.finalViettel)
  viettel: Viettel;
}
