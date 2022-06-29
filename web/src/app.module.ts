import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { MongooseModule } from '@nestjs/mongoose';
import { AppService } from './app.service';
import { App, AppSchema } from './app.schema';
@Module({
  controllers: [AppController],
  imports: [
    MongooseModule.forFeature([{ name: App.name, schema: AppSchema }]),
    MongooseModule.forRoot('mongodb://localhost:27017/test'),
  ],
  providers: [AppService],
})
export class AppModule {}
