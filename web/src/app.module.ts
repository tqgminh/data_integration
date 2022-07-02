import { Module } from '@nestjs/common';

import { AppController } from './app.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { AppService } from './app.service';
import {
  Final,
  CellPhones,
  Didongviet,
  Dienmayxanh,
  FinalCellPhones,
  FinalDidongviet,
  FinalDienmayxanh,
  FinalTgdd,
  FinalTiki,
  FinalViettel,
  Tgdd,
  Tiki,
  Viettel,
} from './app.entity';
@Module({
  controllers: [AppController],
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'localhost',
      port: 5432,
      username: 'postgres',
      password: 'postgres',
      database: 'phone',
      autoLoadEntities: true,
      synchronize: true,
      entities: ['dist/**/**/*.entity{.ts,.js}'],
    }),
    TypeOrmModule.forFeature([
      Final,
      CellPhones,
      Didongviet,
      Dienmayxanh,
      FinalCellPhones,
      FinalDidongviet,
      FinalDienmayxanh,
      FinalTgdd,
      FinalTiki,
      FinalViettel,
      Tgdd,
      Tiki,
      Viettel,
    ]),
  ],
  providers: [AppService],
})
export class AppModule {}
